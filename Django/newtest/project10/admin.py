from django.contrib import admin
from project10.models import GoodsInfo


# Register your models here.

class GoodsAdmin(admin.ModelAdmin):
    list_display = ('goods_name', 'goods_number', 'goods_price')


admin.site.register(GoodsInfo, GoodsAdmin)
