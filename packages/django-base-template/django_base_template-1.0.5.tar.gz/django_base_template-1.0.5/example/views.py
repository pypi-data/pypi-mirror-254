from django.contrib import messages

from django.shortcuts import render

from django.utils.translation import gettext as _, get_language


def index(request, *args, **kwargs):
    messages.success(request, _("This is a message"))
    breadcrumb = [{"title": "Home", "url": "/"}]
    if kwargs.get('id', None):
        breadcrumb.append({"title": f"Page {kwargs.get('id')}", })
    return render(request, 'example/index.html', {
        "title": f"Page {kwargs.get('id')}" if kwargs.get('id', None) else "Home",
        "page": kwargs.get('id', None),
        "breadcrumb": breadcrumb,
        "lang":get_language(),
        "actions": "example/actions.html"
    })
