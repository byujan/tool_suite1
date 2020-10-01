from django.urls import path
from . import views

urlpatterns = [
    path("", views.login, name="login"),
    path("dashboard/", views.index, name="index"),
    path("trollresults/", views.trollresults, name="trollresults"),
]