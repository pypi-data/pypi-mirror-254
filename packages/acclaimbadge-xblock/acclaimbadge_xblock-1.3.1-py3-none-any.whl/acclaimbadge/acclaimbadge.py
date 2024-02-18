from datetime import datetime
import logging
import pytz

from web_fragments.fragment import Fragment
from xblock.core import XBlock
from xblock.fields import Scope, Boolean, String

from xblockutils.studio_editable import StudioEditableXBlockMixin
from xblockutils.resources import ResourceLoader

from xmodule.services import SettingsService

from django.contrib.auth.models import User
from django.test.client import RequestFactory
from django.utils.translation import gettext as _

from lms.djangoapps.grades.course_grade_factory import CourseGradeFactory
from lms.djangoapps.courseware.courses import get_course_with_access

from common.djangoapps.student.models import CourseEnrollment, UserProfile

from .acclaim_client import AcclaimClient, AcclaimClientError

VUE_URL = 'https://cdn.jsdelivr.net/npm/vue@2.6.8/dist/vue.min.js'

log = logging.getLogger(__name__)

loader = ResourceLoader(__name__)

def badge_templates_values_provider(block):
    if block.org_name:
        try:
            client = block._get_acclaim_client()
            templates = client.get_badge_templates(all=True)
            return [{'display_name': t['name'], 'value': t['id']} for t in templates]
        except:
            # we've tried, we've failed...move along...badge template field will be a text field
            pass

    return None

def orgs_options(block):
    return [""] + block._get_org_names()

@XBlock.needs('user')
class AcclaimBadgeXBlock(StudioEditableXBlockMixin, XBlock):
    badge_template_id = String(
        display_name="Badge template ID",
        default='',
        scope=Scope.settings,
        # TODO: there are too many badges in Acclaim, so this request times out
        # values_provider=badge_templates_values_provider
    )

    org_name = String(
        default="",
        scope=Scope.settings,
        display_name="Organization",
        values_provider=orgs_options
    )

    claim_date = String(scope=Scope.user_state)

    editable_fields = ('display_name', 'org_name', 'badge_template_id')
    has_author_view = True

    # Has the learner agreed to send their information for this badge to Credly?
    agreed_to_credly = Boolean(scope=Scope.user_state)

    def student_view(self, context=None):
        html = loader.render_mako_template("static/html/acclaimbadge.html", {
            'ribbon_icon_url': self.runtime.local_resource_url(self, 'public/img/ribbon.png')
        })

        frag = Fragment(html)
        frag.add_css(loader.load_unicode("static/css/acclaimbadge.css"))
        frag.add_javascript_url(VUE_URL)
        frag.add_javascript(loader.load_unicode("static/js/src/acclaimbadge.js"))
        frag.initialize_js('AcclaimBadgeXBlock')

        return frag

    def author_view(self, context=None):
        if self.badge_template_id:
            try:
                client = self._get_acclaim_client()
                badge = client.get_badge_template(self.badge_template_id)
            except AcclaimClientError:
                badge = {}
        else:
            badge = {}

        html = loader.render_mako_template("static/html/acclaimbadge-studio.html", {
            'badge': badge
        })

        frag = Fragment(html)
        frag.add_css(loader.load_unicode("static/css/acclaimbadge.css"))

        return frag

    @XBlock.json_handler
    def get_page_context(self, data, suffix=''):
        context = {}
        student = self._get_current_info()
        enrollment_mode, is_active = CourseEnrollment.enrollment_mode_for_user(student, self.course_id)

        if not enrollment_mode or not is_active:
            context['error'] = _("You are not enrolled in this course or the course doesn't offer a badge.")
            return context

        try:
            client = self._get_acclaim_client()
            badge = client.get_badge_template(self.badge_template_id)
            context['badge'] = badge

            # check if user passed course
            userGradeFactory = CourseGradeFactory().read(student, course_key=self.course_id)
            is_course_passed = userGradeFactory.passed

            if not is_course_passed:
                context['text'] = _("A button to claim your badge will be displayed when you have passed the course.")
                context['show_button'] = False
                return context

            if self.agreed_to_credly and client.has_badge(student.email, badge['id']):
                context['show_button'] = False
                context['show_ribbon'] = True
                context['text'] = _("Congratulations! You've already earned this badge.")

            else:
                context['show_button'] = True
                context['text'] = _("Congratulations! You've earned the {open_badge_name_tag} {badge_name} "
                                        "{close_badge_name_tag} badge! Click the button below to claim it."
                                    ).format(
                                        badge_name=badge.get('name', ''),
                                        open_badge_name_tag='<span class="acclaimbadge acclaimbadge--text-badge-name">',
                                        close_badge_name_tag='</span>')
        except AcclaimClientError as e:
            log.exception("Couldn't build Credly page context")
            msg = getattr(e, "message", None)
            if msg:
                context['error'] = e.message
            else:
                context['error'] = _("There was an error, please refresh the page to try again.")
            return context

        return context

    @XBlock.json_handler
    def request_badge(self, data, suffix=''):
        django_user = self.runtime.service(self, 'user')._django_user

        # TODO: find time course completed to avoid duplicated badges
        if not self.claim_date:
            self.claim_date = datetime.now(pytz.timezone('America/Toronto')).strftime('%Y-%m-%d %H:%M:%S %z')

        self.agreed_to_credly = True

        badge = {
            'recipient_email': django_user.email,
            # This is optional, and if sent, should be an externalized id.
            #'issuer_earner_id': django_user.id,
            'badge_template_id': self.badge_template_id,
            'issued_at': self.claim_date,
            'issued_to_first_name': django_user.profile.name.split(' ',1)[0]
        }

        try:
            client = self._get_acclaim_client()

            if client.has_badge(badge['recipient_email'], badge['badge_template_id']):
                return {'refresh': True}

            badge_resp = client.issue_badge(badge)

            response = {}
            response['badge'] = badge_resp
            response['text'] = _("Congratulations! You earned the {open_badge_name_tag} {badge_name} "
                                    "{close_badge_name_tag} badge! You will receive an email from Credly, our "
                                    "badging partner, confirming your accomplishment."
                                ).format(
                                    badge_name=response['badge']['badge_template']['name'],
                                    open_badge_name_tag='<span class="acclaimbadge acclaimbadge--text-badge-name">',
                                    close_badge_name_tag='</span>')

            return response

        except AcclaimClientError as e:
            return {'error': _('Failed to request badge. Please refresh the page and try again.')}

    def _get_current_info(self):
        xblock_user = self.runtime.service(self, 'user').get_current_user()
        username = xblock_user.opt_attrs['edx-platform.username']

        student = User.objects.get(username=username)

        return student

    def _get_orgs(self):
        service = SettingsService()
        return service.get_settings_bucket(self)

    def _get_org_names(self):
        return list(self._get_orgs().keys())

    def _get_org(self):
        return self._get_orgs().get(self.org_name, {})

    def _get_acclaim_client(self):
        org = self._get_org()
        if not org:
            raise AcclaimClientError("Credly organization not selected: org_name = {!r}.".format(self.org_name))
        return AcclaimClient(org['id'], org['api_key'], org.get('url', None))

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("AcclaimBadgeXBlock",
             """<acclaimbadge/>
             """),
            ("Multiple AcclaimBadgeXBlock",
             """<vertical_demo>
                <acclaimbadge/>
                <acclaimbadge/>
                <acclaimbadge/>
                </vertical_demo>
             """),
        ]
