"""code_hackathon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from charityswipe.views import Interests, Match, Profiles, ProfileInterests, export

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile', Profiles.as_view()),
    path('profile/<id>', ProfileInterests.as_view()),
    path('profile/<id>/match', Match.as_view()),
    path('interests/', Interests.as_view()),
    path('export/', export),
]
