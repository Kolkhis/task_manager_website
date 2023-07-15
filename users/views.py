from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from . import forms
from . import models
import logging

logger = logging.getLogger(__name__)

def dashboard(request):
    return render(request, "users/dashboard.html")


def register(request):
    if request.method == "POST":
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_profile = models.UserProfile(
                user=new_user, date_joined=new_user.date_joined
            )
            new_profile.save()
            login(request, user=new_user)
            messages.success(request, "User successfully created!")
            return redirect("../dashboard")
        else:
            messages.error(request, "There was an error while processing your request.")
            return render(request, "registration/register.html", context={"form": form})
    form = forms.RegistrationForm()
    return render(request, "registration/register.html", context={"form": form})


def edit_profile(request):
    if request.method == "POST":
        form = forms.EditProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user_profile = request.user.profile
            # user_profile = models.UserProfile.objects.filter(id=request.user.id).first()
            # user_profile = forms.EditProfileForm(request.POST, request.FILES)
            user_profile.first_name = form.cleaned_data.get("first_name")
            user_profile.last_name = form.cleaned_data.get("last_name")
            user_profile.occupation = form.cleaned_data.get("occupation")
            user_profile.public_email = form.cleaned_data.get("public_email")
            user_profile.profile_image = form.cleaned_data.get("profile_image")
# Comment out for now - if user wants a blank field, let them have it!
#             user_profile.first_name = form.cleaned_data.get("first_name", user_profile.first_name)
#             user_profile.last_name = form.cleaned_data.get("last_name", user_profile.last_name)
#             user_profile.occupation = form.cleaned_data.get("occupation", user_profile.occupation)
#             user_profile.public_email = form.cleaned_data.get("public_email", user_profile.public_email)
#             user_profile.profile_image = form.cleaned_data.get("profile_image", user_profile.profile_image)
            logger.warning(f'PROFILE IMAGE FIELD RESULT: {form.cleaned_data.get("profile_image")}')
            user_profile.save()
            return redirect(f"../profile/{request.user.username}")
        messages.add_message(request, message="Form was not valid!", level="ERROR")
        return render(request, "users/edit_profile.html", context={"form": form})
    # user_profile = models.UserProfile.objects.filter(id=request.user.id).first()
    form = forms.EditProfileForm(instance=request.user.profile)
    return render(request, "users/edit_profile.html", context={"form": form})


def profile(request, user_name):
    requested_profile = User.objects.filter(username=user_name).first().profile
    return render(
        request,
        "users/profile.html",
        context={"profile": requested_profile, "username": user_name},
    )
