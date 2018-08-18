from django.db import models


# Create your models here.
class GoodsInfo(models.Model):
    goods_name = models.CharField('商品名称',max_length=30, primary_key=True)
    goods_number = models.IntegerField('数量')
    goods_price = models.FloatField('价格')

    class Meta:
        verbose_name_plural = "商品管理"
        verbose_name = "商品"

    def __str__(self):
        return self.goods_name
