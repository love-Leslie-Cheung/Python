from django.shortcuts import render

from MyApp.models import Goods


def test(request):
    return render(request, 'index.html')


def search_all(request):
    goods_list = Goods.objects.all()
    return render(request, 'search_result.html', {'goods_list': goods_list})


def search_name(request):
    goods_name = request.GET['goods_name'].strip()
    goods_list = Goods.objects.filter(goods_name=goods_name)  # 完全匹配搜索关键字
    # goods_list = Goods.objects.filter(goods_name__contains=goods_name)  # 模糊匹配搜索关键字
    return render(request, 'search_result.html', {'goods_list': goods_list})


def search_price(request):
    min_price = request.GET['min_price']
    max_price = request.GET['max_price']
    goods_list = Goods.objects.filter(goods_price__gt=min_price, goods_price__lt=max_price)
    return render(request, 'search_result.html', {'goods_list': goods_list})


def search_sort(request):
    sort = {'all_asc': Goods.objects.order_by('goods_price'),  # 查询全部结果后升序排列
            'all_desc': Goods.objects.order_by('-goods_price'),  # 查询全部结果后降序排列
            'result_asc': Goods.objects.filter(goods_price__lt='5').order_by('goods_price')  # 对某一查询结果排序
            }
    return render(request, 'search_result.html', {'goods_list': sort[request.GET['sort']]})
