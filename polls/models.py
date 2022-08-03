from django.db import models
from django.db.models import CharField

# Create your models here.


class Urls(models.Model):
    password = models.CharField(max_length=100, null=True)
    log = models.CharField(max_length=100, null=True)