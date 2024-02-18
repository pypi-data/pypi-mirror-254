var addConfirmMessageToApp = function () {
  /*
  * Example
   <a href="url/path" // mandatory
      data-request-method="POST" // mandatory
      data-toggle="confirm" // mandatory
      data-confirm-message="Are you sure you would like to do this action!" // mandatory
      class="menu-link px-3 text-danger"
      data-force-reload="false" // optional
      data-as-form="true" // optional, used to normally submit as form
      data-callback="method" // mandatory if force-reload == false
      data-confirm-yes="Yes, Do it!" // optional
      data-confirm-no="No, cancel it!" // optional
      data-confirm-icon="warning" // optional
      data-cancel-message="" // optional
      data-cancel-icon="" // optional
      data-cancel-action="" // optional
  >Action Label</a>
  *
  * Response must return:
  * on success: JsonResponse {message: ""} status 200
  * on failure: JsonResponse {message: ""} status 4XX
  *
  */
  function sendRequest({method, url, forceReload, callback}) {
    $.ajax({
      url: url,
      type: method,
      headers: {
        "X-CSRFToken": csrfToken,
      },
      success: function (res) {
        toastr.success(res['message']);
        if (forceReload)
          location.reload()
        else if (callback && !forceReload) {
          var cb = window,
              callbackSplit = callback.split('.')
          for (var obj of callbackSplit) {
            cb = cb[obj]
          }
          if (typeof cb === 'function') {
            cb.call(res)
          }
          // callback.call()
        }
      },
      error: function (xhr) {
        toastr.error(xhr['responseJSON'].message)
      }
    })
  }

  function showConfirmationPopup(options) {
    var asFormOptions = {}
    if (options.requestParams.asForm)
      asFormOptions = {
        html: `<form action="${options.requestParams.url}" method="${options.requestParams.method}" id="confirm-form-${options.id}">
        <h2>${options.message}</h2>
        <input type="hidden" name="csrfmiddlewaretoken" value="${csrfToken}">
      </form>`,
      }
    return Swal.fire({
      ...asFormOptions,
      text: options.message,
      icon: options.icon,
      showCancelButton: true,
      buttonsStyling: false,
      confirmButtonText: options.yes,
      cancelButtonText: options.no,
      customClass: {
        confirmButton: "btn btn-primary",
        cancelButton: "btn btn-active-light"
      }
    }).then(function (result) {
      if (result.value) {
        if (!options.requestParams.asForm)
          sendRequest(options.requestParams)
        else
          $(`#confirm-form-${options.id}`).submit()
      } else if (result.dismiss === 'cancel') {
        Swal.fire({
          text: options.cancel.text,
          icon: options.cancel.icon,
          buttonsStyling: false,
          confirmButtonText: options.cancel.button,
          customClass: {
            confirmButton: "btn btn-primary",
          }
        });
      }
    });
  }

  function dataAttrExists($el, data) {
    return $el.data(data) !== undefined
  }

  function initConfirmMessage() {
    $(document).on('click', '[data-toggle="confirm"]', function (e) {
      e.preventDefault();
      var $this = $(this),
          options = {
            id: Date.now(),
            message: $this.data('confirm-message'),
            icon: dataAttrExists($this, 'confirm-icon') ? $this.data('confirm-icon') : "warning",
            yes: dataAttrExists($this, 'confirm-yes') ? $this.data('confirm-yes') : gettext('Yes, do it!'),
            no: dataAttrExists($this, 'confirm-no') ? $this.data('confirm-no') : gettext('No, cancel!'),
            cancel: {
              text: dataAttrExists($this, 'cancel-message') ? $this.data('cancel-message') : gettext("Your action will be cancelled!."),
              icon: dataAttrExists($this, 'cancel-icon') ? $this.data('cancel-icon') : "error",
              button: dataAttrExists($this, 'cancel-action') ? $this.data('cancel-action') : gettext("Ok, got it!"),
            },
            requestParams: {
              asForm: dataAttrExists($this, 'as-form') ? $this.data('as-form') : false,
              method: dataAttrExists($this, 'request-method') ? $this.data('request-method') : "GET",
              url: $this.attr('href'),
              forceReload: dataAttrExists($this, 'force-reload') ? Boolean($this.data('force-reload')) : true,
              callback: dataAttrExists($this, 'callback') ? $this.data('callback') : false
            }
          }

      showConfirmationPopup(options)

    })
  }

  return {
    init: function () {

      initConfirmMessage()
    }
  }
}()


if (document.readyState !== 'loading' && document.body) {
  addConfirmMessageToApp.init()
} else {
  document.addEventListener('DOMContentLoaded', addConfirmMessageToApp.init);
}
