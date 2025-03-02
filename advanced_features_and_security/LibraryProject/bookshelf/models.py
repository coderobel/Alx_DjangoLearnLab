from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField
class CustomUser(AbstractUser):
    date_of_birth = models.CharField(max_length=20)
    profile_photo = models.CharField(max_length = 20)