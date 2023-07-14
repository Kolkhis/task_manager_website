from django.urls import path, include
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("register/", views.register, name="register"),
    path("edit_profile/", views.edit_profile, name="edit_profile"),
    path("profile/<user_name>/", views.profile, name="profile"),
]
