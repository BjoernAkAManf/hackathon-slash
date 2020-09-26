from django.db import models
from django.contrib.auth.models import User



class Interest(models.Model):
    name = models.CharField(max_length=150)


class Foundation(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    interests = models.ForeignKey(Interest, on_delete=models.CASCADE, related_name='foundation')

class User(User):
    name = models.CharField(max_length=100)
    interests = models.ManyToManyField(Interest)

# Create your models here.
