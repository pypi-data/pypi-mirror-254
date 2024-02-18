function AcclaimBadgeXBlock(runtime, element) {
  var self = this;

  this.initialContextUrl = runtime.handlerUrl(element, 'get_page_context', '', '', false, 'handler_non_atomic');
  this.requestBadgeUrl = runtime.handlerUrl(element, 'request_badge');
  this.genericErrorMessage = 'Please reload the page to try again.';

  this.app = new Vue({
    el: element,

    data: {
      showLoader: true,
      showButton: true,
      showRibbon: true,
      text: '',
      error: '',
      badge: {}
    },

    methods: {
      requestBadge: function (ev) {
        ev.target.disabled = true;
        self.requestBadgeHandler()
      }
    }
  });

  this.requestBadgeHandler = function () {
    // Claim the badge and updates the app data
    $.post(self.requestBadgeUrl, JSON.stringify({}))
      .done(function (data) {
        if (data.refresh) {
          window.location.reload(true);
          return;
        }

        self.app.text = data.text;
        self.app.showButton = false;
        self.app.showRibbon = true;
      })
      .fail(function () {
        self.app.error = gettext(self.genericErrorMessage);
      });
  };

  this.init = function () {
    // Request initial data from the server and populate app
    $.post(self.initialContextUrl, JSON.stringify({}))
      .done(function (data) {
        self.app.text = data.text;
        self.app.error = data.error;
        self.app.badge = $.isEmptyObject(data.badge) ? null : data.badge;
        self.app.showButton = data.show_button;
        self.app.showRibbon = data.show_ribbon;
      })
      .fail(function () {
        self.app.error = gettext(self.genericErrorMessage);
        self.app.badge = null;
      })
      .always(function () {
        self.app.showLoader = false;
      });
  };

  this.init()
}
