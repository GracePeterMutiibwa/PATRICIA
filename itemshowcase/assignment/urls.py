from django.urls import path

from . import views

# define url patterns 
urlpatterns = [
    path("", views.loadHomePage, name='homepage'),
    path("about/", views.loadAboutPage, name='aboutpage'),
    path("services/", views.loadServicePage, name='servicepage'),
    path("contact/", views.loadContactPage, name='contactpage')
]