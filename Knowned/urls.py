from os import name
from django.urls import path
from Knowned import views
from .views import *



urlpatterns = [
    path("",views.homepage,name="homepage"),
    path("add",views.add,name="add"),
    path("khalti_request",views.khalti_request, name="khalti_request"),
    path("khalti-verify/", KhaltiVerifyView.as_view(), name="khaltiverify"),
    path("about",views.about,name="about")


]