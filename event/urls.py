from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("index", views.index, name="index"),
    path("login", views.login, name="login"),
    path("details", views.details, name="details"),
    path("logout",views.logout, name="logout"),
    path("details1", views.details1, name="details1"),
    path("register", views.register, name="register"),
    path("registered", views.registered, name="registered"),
    path("register1", views.register1, name="register1"),
    path("registered1", views.registered1, name="registered1"),
    path("download",views.download,name="download"),

    path("new_event",views.new_event,name="new_event")
    ]