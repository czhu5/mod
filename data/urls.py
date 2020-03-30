from django.urls import path

from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('import/',views.simple_upload, name='simple_upload'),
    path('about', views.about, name='about'),

]
