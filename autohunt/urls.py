from django.urls import path

from . import views

app_name = 'autohunt'
urlpatterns = [
    # ex: /autohunt/
    path('', views.index, name='index')
]