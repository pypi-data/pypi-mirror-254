import importlib

from django.conf import settings
from django.templatetags.static import static
from django.utils.translation import get_language


def get_settings_value(settings_key, default_value=None):
    return getattr(settings, settings_key, default_value)


def import_class_or_function(name):
    name_split = name.split('.')
    name = name_split[-1:][0]
    module_name = name_split[:-1]
    return getattr(importlib.import_module('.'.join(module_name)), name)


def get_class_from_settings(settings_key, default_class=None):
    class_name = get_settings_value(settings_key, None)

    if not class_name:
        class_name = default_class

    return import_class_or_function(class_name) if type(class_name) is str else class_name


def register_sidebar_item(
        order, title, icon=None, url=None, is_active=False, permissions=None, children=None, comment=None,
        is_child=False):
    sidebar_item = {
        "order": order,
        "title": title,
        "icon": icon,
        "url": url,
        "is_active": is_active,
        "permissions": permissions,
        "has_children": False,
        "comment": comment,
        "children": children if children else [],
    }

    if is_child:
        sidebar_item.pop('icon', None)

    if children:
        sidebar_item["has_children"] = True
        sidebar_item.pop('comment', None)

    return sidebar_item


def register_sidebar_label(order, title, permissions):
    sidebar_label = {
        "order": order,
        "title": title,
        "permissions": permissions,
        "is_label": True
    }
    return sidebar_label


def get_assets(request):
    css = [
        {
            "rel": "short icon",
            "href": static("base_template/images/icon.ico")
        },
        {
            "rel": "stylesheet",
            "href": "https://fonts.googleapis.com/css?family=Inter:300,400,500,600,700"
        }
    ]
    js = [
        static("base_template/plugins/global/plugins.bundle.js"),
        static("base_template/js/scripts.bundle.js"),
        static("base_template/js/utils.js")
    ]
    if get_settings_value("BASE_TEMPLATE_MULTIPLE_LANGUAGES", False):
        from django.urls import reverse
        js.insert(0, reverse("javascript-catalog"))
    if get_language() in settings.LANGUAGES_BIDI:
        css.append({
            "rel": "stylesheet",
            "href": static("base_template/plugins/global/plugins.bundle.rtl.css"),
            "type": "text/css"
        })
        css.append({
            "rel": "stylesheet",
            "href": static("base_template/css/style.bundle.rtl.css"),
            "type": "text/css"
        })
    else:
        css.append({
            "rel": "stylesheet",
            "href": static("base_template/plugins/global/plugins.bundle.css"),
            "type": "text/css"
        })
        css.append({
            "rel": "stylesheet",
            "href": static("base_template/css/style.bundle.css"),
            "type": "text/css"
        })
    return {"css": css, "js": js}

