from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from . import forms
from . import models


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
            # user_profile = forms.EditProfileForm(request.POST, request.FILES)
            user_profile.first_name = form.cleaned_data.get("first_name")
            user_profile.last_name = form.cleaned_data.get("last_name")
            user_profile.occupation = form.cleaned_data.get("occupation")
            user_profile.public_email = form.cleaned_data.get("public_email")
            # user_profile.profile_image = request.FILES.get('profile_image')
            user_profile.profile_image = form.cleaned_data.get("profile_image")
            user_profile.save()
            return redirect(f"../profile/{request.user.username}")
        messages.add_message(request, message="Form was not valid!", level="ERROR")
        return render(request, "users/edit_profile.html", context={"form": form})
    form = forms.EditProfileForm()
    return render(request, "users/edit_profile.html", context={"form": form})


def profile(request, user_name):
    requested_profile = User.objects.filter(username=user_name).first().profile
    return render(
        request,
        "users/profile.html",
        context={"profile": requested_profile, "username": user_name},
    )
