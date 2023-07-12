from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from . import models


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class EditProfileForm(ModelForm):
    class Meta:
        model = models.UserProfile
        fields = [
            "first_name",
            "last_name",
            "occupation",
            "public_email",
            "profile_image",
        ]

