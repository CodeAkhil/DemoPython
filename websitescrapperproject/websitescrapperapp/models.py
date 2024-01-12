from django.db import models

# Create your models here.


class Links(models.Model):
    objects = None
    address = models.CharField(max_length=500, null=True, blank=True)
    stringname = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.stringname
