import sys
import logging

import requests

PRODUCTION_URL = "https://www.youracclaim.com/api/v1"

log = logging.getLogger(__name__)

class AcclaimClient:
    def __init__(self, org_id, api_key, base_url, timeout=5):
        self.org_id = org_id
        self.api_key = api_key
        self.base_url = base_url if base_url else PRODUCTION_URL
        self.timeout = timeout

    def get_url(self, path):
        return "{0}/organizations/{1}/{2}".format(self.base_url, self.org_id, path.lstrip('/'))

    def get_badge_templates(self, page=1, all=False):
        url = self.get_url('/badge_templates')
        r = requests.get(url, auth=(self.api_key, ''), params={'page': page, 'sort': 'name'}, timeout=self.timeout)
        new_templates = self._handle_response(r)
        if not all:
            return new_templates

        templates = []
        while len(new_templates) > 0:
            templates += new_templates
            page += 1
            new_templates = self.get_badge_templates(page=page)

        return templates

    def get_badge_template(self, badge_template_id):
        url = self.get_url('/badge_templates/{0}'.format(badge_template_id))
        r = requests.get(url, auth=(self.api_key, ''), timeout=self.timeout)
        return self._handle_response(r)

    def issue_badge(self, badge):
        url = self.get_url('/badges')
        r = requests.post(url, auth=(self.api_key, ''), json=badge, timeout=self.timeout)
        return self._handle_response(r)

    def has_badge(self, email, badge_template_id):
        url = self.get_url('/badges')
        params = {
            'filter': "recipient_email::{0}|badge_template_id::{1}".format(email, badge_template_id)
        }

        r = requests.get(url, auth=(self.api_key, ''), params=params, timeout=self.timeout)
        response = self._handle_response(r)
        return len(response) > 0 and response[0].get('state', '') != 'revoked'

    def _handle_response(self, resp):
        json = resp.json()

        if 200 <= resp.status_code < 300:
            log.info(json)

            if json and 'data' in json:
                return json['data']
            else:
                return json
        else:
            log.error(json)
            raise AcclaimClientError(json.get('message', None), resp.status_code)

class AcclaimClientError(Exception):
    def __init__(self, message, status_code=None):
        super(Exception, self).__init__(message)

        self.status_code = status_code
