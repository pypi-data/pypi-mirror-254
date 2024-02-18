from django.apps import AppConfig
from django.urls import reverse

from src.base_template.utils import register_sidebar_label, register_sidebar_item


class ExampleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'example'

    def get_main_sidebar(self, request):
        return [
            register_sidebar_label(
                order=1,
                title="Main Label 1",
                permissions=True
            ),
            register_sidebar_item(
                order=2,
                title="Main Item 2",
                icon='<i class="ki-duotone ki-element-11 fs-2"><i class="path1"></i><i class="path2"></i><i class="path3"></i><i class="path4"></i></i>',
                is_active=request.path in [
                    reverse('home-id', args=[21]),
                    reverse('home-id', args=[22])
                ],
                permissions=True,
                children=[
                    register_sidebar_item(
                        order=1,
                        title="Main Item 2 Child 1",
                        url=reverse('home-id', args=[21]),
                        is_active=request.path == reverse('home-id', args=[21]),
                        permissions=True,
                        comment="Main Item 2 Child 1",
                    ),
                    register_sidebar_item(
                        order=2,
                        title="Main Item 2 Child 2",
                        url=reverse('home-id', args=[22]),
                        is_active=request.path == reverse('home-id', args=[22]),
                        permissions=True,
                        comment="Main Item 2 Child 2",
                    ),
                ]
            ),
            register_sidebar_item(
                order=3,
                title="Main Item 3",
                icon='<i class="ki-duotone ki-abstract-41 fs-2"><i class="path1"></i><i class="path2"></i></i>',
                url=reverse('home-id', args=[3]),
                is_active=request.path == reverse('home-id', args=[3]),
                permissions=True,
                comment="Main Item 3",
            ),
            register_sidebar_item(
                order=4,
                title="Main Item 4",
                icon='<i class="ki-duotone ki-abstract-41 fs-2"><i class="path1"></i><i class="path2"></i></i>',
                url=reverse('home-id', args=[4]),
                is_active=request.path == reverse('home-id', args=[4]),
                permissions=False,
                comment="Main Item 4",
            ),
            register_sidebar_label(
                order=5,
                title="Main Label 2",
                permissions=True
            ),
            register_sidebar_item(
                order=6,
                title="Main Item 2",
                icon='<i class="ki-duotone ki-abstract-15 fs-2"><i class="path1"></i><i class="path2"></i></i>',
                is_active=request.path in [
                    reverse('home-id', args=[61]),
                    reverse('home-id', args=[62])
                ],
                permissions=True,
                children=[
                    register_sidebar_item(
                        order=1,
                        title="Main Item 6 Child 1",
                        url=reverse('home-id', args=[61]),
                        is_active=request.path == reverse('home-id', args=[61]),
                        permissions=True,
                        comment="Main Item 6 Child 1",
                    ),
                    register_sidebar_item(
                        order=2,
                        title="Main Item 6 Child 2",
                        url=reverse('home-id', args=[62]),
                        is_active=request.path == reverse('home-id', args=[62]),
                        permissions=True,
                        comment="Main Item 6 Child 2",
                    ),
                ]
            ),
            register_sidebar_item(
                order=7,
                title="Main Item 7",
                icon='<i class="ki-duotone ki-abstract-29 fs-2"><i class="path1"></i><i class="path2"></i></i>',
                url=reverse('home-id', args=[7]),
                is_active=request.path == reverse('home-id', args=[7]),
                permissions=True,
                comment="Main Item 7",
            ),
            register_sidebar_item(
                order=8,
                title="Main Item 8",
                icon='<i class="ki-duotone ki-abstract-16 fs-2"><i class="path1"></i><i class="path2"></i></i>',
                url=reverse('home-id', args=[8]),
                is_active=request.path == reverse('home-id', args=[8]),
                permissions=False,
                comment="Main Item 8",
            )
        ]

    def get_before_content(self, request):
        return [
            {"template_name": "example/alerts_without_context.html", },
            {
                "template_name": "example/alerts_with_context.html",
                "context": {
                    "items": [
                        {"title": "This is an alert",
                         "description": "The alert component can be used to highlight certain parts of your page for higher content visibility."},
                        {"title": "This is an alert",
                         "description": "The alert component can be used to highlight certain parts of your page for higher content visibility."},
                        {"title": "This is an alert",
                         "description": "The alert component can be used to highlight certain parts of your page for higher content visibility."},
                        {"title": "This is an alert",
                         "description": "The alert component can be used to highlight certain parts of your page for higher content visibility."},
                        {"title": "This is an alert",
                         "description": "The alert component can be used to highlight certain parts of your page for higher content visibility."},
                    ]
                }
            },
        ]
