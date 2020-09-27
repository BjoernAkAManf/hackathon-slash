from django.contrib import admin

# Register your models

from django.contrib import admin
from .models import Profile, Foundation, Interest

admin.site.register(Foundation)
admin.site.register(Interest)
admin.site.register(Profile)