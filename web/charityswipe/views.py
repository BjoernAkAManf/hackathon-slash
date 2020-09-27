import os
import json
from django.core import serializers
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.forms.models import model_to_dict
from django.views import View
from .models import Interest, Foundation, Profile

class Profiles(View):
    def post(self, request, *args, **kwargs):
        m = Profile()
        m.save()
        k = model_to_dict(m)
        return JsonResponse(k, safe=False)

class ProfileInterests(View):
    def put(self, request, *args, **kwargs):
        try:
            v = json.loads(request.body.decode('utf-8'))
            if not isinstance(v, list):
                return HttpResponse('Error 2')
            user = Profile.objects.get(uuid=kwargs['id'])
            for i in list(user.interests.all()):
                user.interests.remove(i)
            for i in list(Interest.objects.filter(id__in=v)):
                user.interests.add(i)
        except:
            return HttpResponse('Error')

        return JsonResponse(zzz(user))

class Interests(View):
    def get(self, request, *args, **kwargs):
        data = list(Interest.objects.all().values())
        return JsonResponse(data, safe=False)

def zzz(z):
    z = model_to_dict(z)
    z['interests'] = list(map(model_to_dict, z['interests']))
    return z

class Match(View):
    def get(self, request, *args, **kwargs):
        user = Profile.objects.get(uuid=kwargs['id'])
        try:
            v = json.loads(request.body.decode('utf-8'))
            if not isinstance(v, list):
                return HttpResponse('Error 2')
            z = Interest.objects.filter(profile__exact=user)
            x = Foundation.objects.filter (interests__in=z).distinct()
            # .all().filter(name__exact="X").values()
            x = list(map(zzz, x))
            print(x)
            return JsonResponse(x, safe=False)
        except:
            return HttpResponse('Error')
            # error
            # return JsonResponse(v, safe=False)

def export(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    fsock = open(os.path.join(BASE_DIR, 'db.sqlite3'),"rb")
    resp = HttpResponse(fsock, content_type='application/octet-stream')
    resp['Content-Disposition'] = 'attachment; filename=db.sqlite3'
    return resp
