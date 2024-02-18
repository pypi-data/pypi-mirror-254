from django.urls import path

from example.views import index

urlpatterns = [
    path('', index, name='home'),
    path('<int:id>/', index, name="home-id"),
]
