
import uuid
from django.db import models
#from django.contrib.auth.models import User

class Interest(models.Model):
    name = models.CharField(max_length=150)
    def __str__(self):
        return self.name


class Foundation(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    interests = models.ManyToManyField(Interest)
    location = models.CharField(max_length=200)
    iban = models.CharField(max_length=40)
    image = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Profile(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=100, default = 'anonymous')
    interests = models.ManyToManyField(Interest)

    def __str__(self):
        return '%s - %s' % (self.uuid, self.name)

# Create your models here.
