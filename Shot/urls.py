from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('profile/',views.profile , name = "profile"),
    path('contact/',views.contact,name="contact"),
    path('contact_sucess/',views.contact1,name="contact1"),
    path('about/',views.about,name="about"),
]