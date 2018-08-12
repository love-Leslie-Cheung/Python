from pyecharts import Bar

def first_charts():
	bar = Bar('我的第一个图表','这里是副标题')
	bar.add('文字',['一','二',"三","四","五","六"],[12,65,32,91,46,35])
	bar.add('服装',['衬衫','羊毛衫',"雪纺衫","裤子","高跟鞋","袜子"],[5, 20, 36, 10, 75, 90],is_more_utils=True)
	bar.show_config()
	bar.render()

def second_charts():
	bar = Bar('我的第二个图表','Evaporation and precipitation')
	attr = ['{}月'.format(i) for i in range(1,13)]
	v1 = [2.0,4.9,7.0,23.2,25.6,76.3,135.6,162.2,32.5,20.0,6.4,3.3]
	v2 = [2.6,5.9,26.6,28.9,9.0,70.0,175.6,192.8,43.2,19.6,6.0,2.3]
	bar.add('蒸发量',attr,v1,mark_line=['average'],mark_point=['max','min'])
	bar.add('降水量',attr,v2,mark_line=['average'],mark_point=['max','min'])
	bar.show_config()
	bar.render()





if __name__ == '__main__':
	# first_charts()
	second_charts()