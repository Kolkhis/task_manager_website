
#########       redirect() as a function         ############
# redirect() can take either relative URL path, or the NAME (in urls.py) of a view.


"""in urls.py"""
from django.urls import path, include
from . import views

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
]


"""in views.py"""
from django.shortcuts import redirect, render

def dashboard(request):
    return redirect("dashboard")


def dashboard2(request):
    return redirect("../dashboard")
