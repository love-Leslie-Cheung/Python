import json
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render

from project10.models import GoodsInfo


def goodslist(request):
    result = GoodsInfo.objects.all()
    return render(request, 'goods_list.html', {'goods_list': result})


def add(request):
    goods_name = request.GET['goods_name']
    goods_price = request.GET['goods_price']
    goods_number = request.GET['goods_number']
    isexist = GoodsInfo.objects.filter(goods_name=goods_name)
    try:
        if not isexist:
            goodsinfo = GoodsInfo()
            goodsinfo.goods_name = goods_name
            goodsinfo.goods_price = goods_price
            goodsinfo.goods_number = goods_number
            goodsinfo.save()
            result = 200
        else:
            result = 100
    except:
        result = 100
    return HttpResponse(result)


def delete(request):
    goods_name = request.GET['goods_name']
    goods = GoodsInfo.objects.filter(goods_name=goods_name)
    try:
        goods.delete()
        result = 200
    except:
        result = 100
    return HttpResponse(result)


def search(request):
    min_price = int(request.GET['min_price'])
    max_price = int(request.GET['max_price'])
    goods = GoodsInfo.objects.filter(goods_price__gte=min_price,goods_price__lte=max_price)
    try:
        if goods:
            result = json.dumps(serializers.serialize('json', goods))
        else:
            result = 100
    except:
        result = 100
    print(result)
    return HttpResponse(result)