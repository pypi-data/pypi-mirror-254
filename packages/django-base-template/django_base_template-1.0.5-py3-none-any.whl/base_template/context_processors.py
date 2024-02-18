from django.apps import apps

from .utils import get_class_from_settings, get_settings_value


def get_menu_from_apps(request, menu):
    # Create the name of the method to call in each app's AppConfig instance.
    menu = "get_{}_sidebar".format(menu)

    # Get a list of all application configurations (AppConfig objects).
    all_apps_conf = apps.get_app_configs()

    # Initialize an empty list to store the sidebar items.
    sidebar_list = []

    # Iterate through each app's AppConfig object.
    for app_conf in all_apps_conf:
        # Check if the app's AppConfig instance has the method corresponding to the menu name and if it's callable.
        if hasattr(app_conf, menu) and callable(getattr(app_conf, menu)):
            # Call the method in the AppConfig instance to get the sidebar items.
            items = getattr(app_conf, menu)(request)

            # If the returned items are a list, append them to the sidebar_list.
            if type(items) == list:
                sidebar_list = sidebar_list + items
            else:
                # If the returned items are not a list, assume it's a single dictionary and append it.
                sidebar_list.append(items)

    # Sort the sidebar items based on the 'order' key in each dictionary.
    sidebar_list = sorted(sidebar_list, key=lambda d: d['order'])

    # Return the final unified and sorted sidebar list.
    return sidebar_list


def get_sidebar(request):
    sidebar = get_class_from_settings("BASE_TEMPLATE_GET_SIDEBAR_METHOD")(request)
    allowed_sidebar = []
    for item in sidebar:
        if item['permissions']:
            if 'children' in item and len(item['children']) > 0:
                allowed_items = []
                for sub_item in item['children']:
                    allowed_items.append(sub_item)
                item['children'] = allowed_items
        allowed_sidebar.append(item)

    return allowed_sidebar


def get_assets(request):
    return get_class_from_settings("BASE_TEMPLATE_GET_ASSETS_METHOD")(request)


def get_before_content_templates(request):
    all_apps_conf = apps.get_app_configs()
    alerts_list = []
    for app_conf in all_apps_conf:
        if hasattr(app_conf, "get_before_content") and callable(getattr(app_conf, "get_before_content")):
            items = getattr(app_conf, "get_before_content")(request)
            if type(items) == list:
                alerts_list = alerts_list + items
            else:
                alerts_list.append(items)

    return alerts_list


def base_template(request):
    return {
        "assets": get_settings_value("BASE_TEMPLATE_ASSETS", get_assets(request)),
        "multiple_languages": get_settings_value("BASE_TEMPLATE_MULTIPLE_LANGUAGES", False),
        "before_content": get_before_content_templates(request),
        "sidebar": {
            "menu": get_sidebar(request),
            "logo": get_settings_value("BASE_TEMPLATE_SIDEBAR_LOGO", None),
            "logo_icon": get_settings_value("BASE_TEMPLATE_SIDEBAR_LOGO_ICON", None),
            "footer": get_settings_value("BASE_TEMPLATE_SIDEBAR_FOOTER_TEMPLATE", None),
        },
        "header": {
            "logo": get_settings_value("BASE_TEMPLATE_HEADER_LOGO", None),
            "right_menus": get_settings_value("BASE_TEMPLATE_HEADER_RIGHT_MENUS", None),
            "left_menus": get_settings_value("BASE_TEMPLATE_HEADER_LEFT_MENUS", None),
        },
        "right_drawers": get_settings_value("BASE_TEMPLATE_RIGHT_DRAWERS", []),
        "footer": {
            "links_template_name": get_settings_value("BASE_TEMPLATE_LINKS_TEMPLATE", None),
            "copyrights": get_settings_value("BASE_TEMPLATE_COPYRIGHTS", None),
        }
    }
