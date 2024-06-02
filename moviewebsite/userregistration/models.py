from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    objects = None
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profession = models.TextField(blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    mobile = models.CharField(max_length=10, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='dp', blank=True, null=True, default='avatar.jpg')

    def __str__(self):
        return self.user.username
