from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 200)
    content = models.Textfield()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey
