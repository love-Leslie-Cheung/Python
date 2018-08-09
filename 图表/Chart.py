import matplotlib.pyplot as plt
from random import randint
import pygal
import json
from pygal_maps_world.i18n import COUNTRIES
from pygal.maps.world import COUNTRIES

# 安装及使用方式
# pip install pygal_maps_world
# import pygal.maps.world
# wm = pygal.maps.world.World()

# 折线图
def linechart():
	input_squares = [1,2,3,4,5]
	squares = [1,4,9,16,25]
	plt.plot(input_squares,squares,linewidth=5)
	# 设置图表标题，并给坐标轴加上标签
	plt.title('Squares Numbers',fontsize=24)
	plt.xlabel('Value',fontsize=14)
	plt.ylabel('Squares of Value',fontsize=14)
	# 设置刻度标记的大小
	plt.tick_params(axis='both',labelsize=14)

	plt.show()

# 单个散点图
def scatterChart_single():
	plt.scatter(2,4)

	plt.title('Squares Numbers',fontsize=24)
	plt.xlabel('Value',fontsize=14)
	plt.ylabel('Squares of Value',fontsize=14)

	plt.tick_params(axis='both',which='major',labelsize=14)	

	plt.show()

# 散点图
def scatterChart():
	x_values = [1,2,3,4,5]
	y_values = [1,4,9,16,25]
	plt.scatter(x_values,y_values,s=100)

	plt.title('Squares Numbers',fontsize=24)
	plt.xlabel('Value',fontsize=14)
	plt.ylabel('Squares of Value',fontsize=14)
	plt.tick_params(axis='both',which='major',labelsize=14)

	plt.show()

# 自动计算数据
def auto_scatter():
	x_values = list(range(1,1001))
	y_values = [x**2 for x in x_values]
	plt.scatter(x_values,y_values,s=10)

	plt.title('Squares Numbers',fontsize=24)
	plt.xlabel('Value',fontsize=14)
	plt.ylabel('Squares of Value',fontsize=14)

	# 设置每个坐标轴的取值范围
	plt.axis([0,1100,0,1100000])

	plt.show()

# 直方图
def histogram(s,num,title,xtitle,ytitle):
	max_num = num
	frequencies = []
	for i in range(0,max_num):
		frequency = s[i]
		frequencies.append(frequency[1])
	# print(frequencies)
	# 对结果进行可视化
	hist = pygal.Bar()
	hist.x_labels = [s[j][0] for j in range(0,max_num)]
	hist.x_title = xtitle
	hist.y_title = ytitle

	hist.add(title,frequencies)
	hist.render_to_file('test.svg')

# 直方图
# 掷骰子，从1~6中选出一个随机数，多次循环，查看各值的频率
def histogram_single():
	max_num = 6
	result = []
	for i in range(1,101):
		result.append(randint(1,max_num))
	print(result)
	frequencies = []
	for i in range(1,max_num+1):
		frequency = result.count(i)
		frequencies.append(frequency)
	print(frequencies)
	# 对结果进行可视化
	hist = pygal.Bar()
	hist.x_labels = ['1','2','3','4','5','6']
	hist.x_title = 'Result'
	hist.y_title = 'Frequency of Result'

	hist.add('D6',frequencies)
	hist.render_to_file('die_visual.svg')

# 直方图
# 掷两个骰子，从1~6中选出一个随机数，多次循环，查看各值的频率
def histogram_double():
	max_num = 6
	result = []
	for i in range(1,1001):
		result.append(randint(1,max_num)+randint(1,max_num))
	frequencies = []
	for i in range(2,max_num*2+1):
		frequency = result.count(i)
		frequencies.append(frequency)
	# 结果可视化
	hist = pygal.Bar()
	hist.x_labels = range(2,max_num*2+1)
	hist.x_title = 'Result'
	hist.y_title = 'Frequency of Value'

	hist.add('D6 + D6',frequencies)
	hist.render_to_file('die_visual.svg')

# 获取两个字母的国别码
def get_country(country):
	try:
		a = list(COUNTRIES.keys())[list(COUNTRIES.values()).index (country)]
	except Exception:
		return None
	else:
		return a	


# 世界人口图
def population():
	# 获取人口信息
	with open('../other/population_json.json','r+') as file:
		pop_data = json.load(file)
	# print(pop_data)
	cc_populations = {}
	for pop_dict in pop_data:
		if pop_dict['Year'] == 2016:
			country_code = get_country(pop_dict['Country Name'])
			pop_value = int(pop_dict['Value'])
			if country_code:
				cc_populations[country_code] = pop_value

	#  根据人口数量将所有的国家分成三组
	cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
	for cc, pop in cc_populations.items():
		if pop < 10000000:
			cc_pops_1[cc] = pop
		elif pop < 1000000000:
			cc_pops_2[cc] = pop
		else:
			cc_pops_3[cc] = pop

	# 制作地图
	wm = pygal.maps.world.World()
	wm.title = 'World Population in 2016, by Country'
	wm.add('0-10m', cc_pops_1)
	wm.add('10m-1bn', cc_pops_2)
	wm.add('>1bn', cc_pops_3)
	# wm.add('2016',cc_populations)
	# wm.add('Asia',['cn','pk','np','th','kp','kr'])
	# wm.add('North America', ['ca', 'mx', 'us'])
	wm.render_to_file('americas.svg')













# ---------------- 测试 ---------------------#
if __name__ == '__main__':
	# linechart()
	# scatterChart_single()
	# scatterChart()
	# auto_scatter()
	# histogram()
	# histogram_single()
	# histogram_double()
	population()
	# print(COUNTRIES)