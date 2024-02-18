# Package Settings
# localization
from django.utils.translation import gettext_lazy as _

BASE_TEMPLATE_MULTIPLE_LANGUAGES = True

BASE_TEMPLATE_APP_NAME = _("Base Template")

# Sidebar
BASE_TEMPLATE_GET_SIDEBAR_METHOD = 'base_template.sidebars.get_sidebar'
BASE_TEMPLATE_GET_ASSETS_METHOD = 'src.base_template.utils.get_assets'
BASE_TEMPLATE_SIDEBAR_FOOTER_TEMPLATE = "base_template/layout/partials/sidebar/_footer.html"
BASE_TEMPLATE_SIDEBAR_LOGO = "base_template/images/logo-white.svg"
BASE_TEMPLATE_SIDEBAR_LOGO_ICON = "base_template/images/icon.svg"

# header
BASE_TEMPLATE_HEADER_LOGO = "base_template/images/logo-dark.svg"
BASE_TEMPLATE_HEADER_LEFT_MENUS = [
    {"order": 0, "template_name": "base_template/partials/menus/_sample_right_menu.html"}
]
BASE_TEMPLATE_HEADER_RIGHT_MENUS = [
    {"order": 0, "template_name": "base_template/partials/theme-mode/_main.html"},
    {"order": 1, "template_name": "base_template/partials/menus/_user-account-menu.html"},
]

# toolbar
BASE_TEMPLATE_TOOLBAR_FIXED = False

# right drawers
BASE_TEMPLATE_RIGHT_DRAWERS = []

# footer
BASE_TEMPLATE_LINKS_TEMPLATE = 'base_template/layout/partials/footer/__footer_links.html'
BASE_TEMPLATE_COPYRIGHTS = {"text": _("Fritill"), "url": "https://fritill.com"}
