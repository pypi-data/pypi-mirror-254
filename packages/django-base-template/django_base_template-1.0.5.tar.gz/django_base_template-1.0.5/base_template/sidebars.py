from src.base_template.context_processors import get_menu_from_apps


def get_sidebar(request):
    return get_menu_from_apps(request, 'main')
