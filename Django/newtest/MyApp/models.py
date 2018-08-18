from django.db import models


# Create your models here.
class Goods(models.Model):
    goods_name = models.CharField(max_length=30)
    goods_number = models.IntegerField()
    goods_price = models.FloatField()
