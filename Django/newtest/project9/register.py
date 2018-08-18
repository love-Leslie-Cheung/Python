from django.http import HttpResponse
from django.shortcuts import render
from project9.models import Users
import json


def reg(request):
    return render(request, 'register.html')


def check(request):
    user_name = request.GET['user_name']
    user = Users.objects.filter(user_name=user_name)
    if user:
        status = 100  # 返回表示已注册的编号
    else:
        status = 200  # 返回表示未注册的编号
    return HttpResponse(status)


def register(request):
    user_name = request.GET['user_name']
    password = request.GET['password']
    try:
        print(user_name , password)
        user = Users(user_name=user_name, password=password)
        user.save()
        status = 200
    except:
        status = 100
    return HttpResponse(json.dumps({'status': status}))
