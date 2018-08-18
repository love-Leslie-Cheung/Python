import os
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newtest.settings')  # 关联默认设置
django.setup()  # 装载Django

from project10.models import GoodsInfo
	
with open('data', 'r', encoding='utf-8') as file:  # 打开文件创建文件对象（注意编码）
	for line in file:  # 读取每一行
		lst = line.strip().split(',')  # 将每一行中的商品信息转换为列表
		state = GoodsInfo.objects.create(goods_name=lst[0], goods_number=lst[1], goods_price=lst[2])  # 添加数据到数据库
		print(state)  # 显示输出添加数据的结果