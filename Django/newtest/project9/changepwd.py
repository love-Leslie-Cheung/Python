from django.http import HttpResponse
from django.shortcuts import render
from project9.models import Users
import json


def change(request):
    return render(request, 'change.html')


def changepwd(request):
    user_name = request.GET['user_name']
    password = request.GET['password']
    user = Users.objects.filter(user_name=user_name)
    try:
        user.update(password=password)
        status = 200
    except:
        status = 100
    return HttpResponse(json.dumps({'status': status}))
