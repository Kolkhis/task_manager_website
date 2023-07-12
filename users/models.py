from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class UserProfile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='profile', null=True, blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    occupation = models.CharField(max_length=50, blank=True)
    public_email = models.EmailField(max_length=254, blank=True)
    date_joined = models.DateTimeField(default=timezone.now)
    # TODO: Create a form/view for this model
    profile_image = models.ImageField(blank=True, upload_to='uploads/',
                                      default=None)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    


