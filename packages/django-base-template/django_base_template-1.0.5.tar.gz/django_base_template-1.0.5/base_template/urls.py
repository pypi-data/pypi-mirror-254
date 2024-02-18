from django.urls import path, include
from django.views.i18n import JavaScriptCatalog



urlpatterns = [
    path('', include('example.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
]
