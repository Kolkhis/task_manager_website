from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class UserProfile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    date_created = models.DateTimeField(default=timezone.now)
    # TODO: Create an option for user to upload a profile picture
    


