from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("home/",views.index, name='home'),
    path("about/",views.about, name='about'),
    path("contact/",views.contact, name='contact'),
    path("services/",views.services, name='services'),
    path("signup/",views.sign_up, name='signup'),
    path("login/",views.user_login, name='login'),
    path("profile/",views.user_profile, name='profile'),
    path('logout/',views.user_logout,name="logout"),
]
