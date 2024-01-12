from django.db import models

# Create your models here.


class Register(models.Model):
    objects = None
    # name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='Click')
    # desc = models.TextField()

    # def __str__(self):
    #     return self.img
