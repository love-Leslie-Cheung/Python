from pyecharts import Bar
from pyecharts import Pie
from pyecharts import Line,Overlap
from random import randint
from pyecharts import Geo
from pyecharts import GeoLines,Style

# 柱状图
def first_charts():
	bar = Bar('我的第一个图表','这里是副标题',page_title='first charts')
	bar.use_theme('dark')
	bar.add('文字',['一','二',"三","四","五","六"],[12,65,32,91,46,35],is_more_utils=True)
	bar.add('服装',['衬衫','羊毛衫',"雪纺衫","裤子","高跟鞋","袜子"],[5, 20, 36, 10, 75, 90],is_convert=True)
	bar.show_config()
	bar.render()

# 柱状/条形图
def second_charts():
	bar = Bar('我的第二个图表','Evaporation and precipitation')
	attr = ['{}月'.format(i) for i in range(1,13)]
	v1 = [2.0,4.9,7.0,23.2,25.6,76.3,135.6,162.2,32.5,20.0,6.4,3.3]
	v2 = [2.6,5.9,26.6,28.9,9.0,70.0,175.6,192.8,43.2,19.6,6.0,2.3]
	bar.add('蒸发量',attr,v1,mark_line=['average'],mark_point=['max','min'])
	bar.add('降水量',attr,v2,mark_line=['average'],mark_point=['max','min'])
	bar.show_config()
	bar.render()

# dataZoom 效果，'both' 类型
def my_bar():
	attr = ["{}天".format(i) for i in range(1,31)]
	v1 = [randint(1, 30) for _ in range(30)]
	bar = Bar("Bar - datazoom - inside 示例")
	bar.add("",attr,v1,is_datazoom_show=True,datazoom_type="both",datazoom_range=[10, 25],)
	bar.render()

# 饼图
def my_pie():
	attr = ['衬衫','羊毛衫',"雪纺衫","裤子","高跟鞋","袜子"]
	v1 = [11,12,13,10,10,10]
	v2 = [19,21,32,20,20,33]
	pie = Pie('饼图-玫瑰图示例',title_pos='center',width=900)
	pie.add('商品A',attr,v1,center=[25,50],is_randon=True,radius=[30,75],rosetype='redius')
	pie.add('商品B',attr,v2,center=[75,50],is_randon=True,radius=[30,75],rosetype='area',is_legend_show=False,is_label_show=True)
	pie.render()

# 折线/面积图
def my_line():
	attr = ['A','B','C','D','E','F']
	v1 = [10,20,30,40,50,60]
	v2 = [38,28,58,48,78,68]
	bar = Bar("Line - Bar 示例")
	bar.add("bar",attr,v1)
	line = Line()
	line.add("line",attr,v2)

	overlap = Overlap()
	overlap.add(bar)
	overlap.add(line)
	overlap.render()




def my_Geolines():
	style = Style(
	    title_top="#fff",
	    title_pos = "center",
	    width=1200,
	    height=600,
	    background_color="#404a59"
	)

	style_geo = style.add(
	    is_label_show=True,
	    line_curve=0.2,
	    line_opacity=0.6,
	    legend_text_color="#eee",
	    legend_pos="right",
	    geo_effect_symbol="plane",
	    geo_effect_symbolsize=15,
	    label_color=['#a6c84c', '#ffa022', '#46bee9'],
	    label_pos="right",
	    label_formatter="{b}",
	    label_text_color="#eee",
	)
	data_guangzhou = [
	    ["珠海", "番禺区",55],
	    ["番禺区", "天河区",6],
	    ["天河区", "南昌",259]
	]
	geolines = GeoLines("GeoLines 示例", **style.init_style)
	geolines.add("从广州出发", data_guangzhou,tooltip_formatter="{a} : {c}", **style_geo)
	geolines.render()




if __name__ == '__main__':
	# first_charts()
	# second_charts()
	# my_bar()
	# my_pie()
	# my_line()
	my_Geolines()