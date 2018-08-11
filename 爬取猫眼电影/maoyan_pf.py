import requests
import re
import json
import pygal

def get_day(url,date):
    url = url + '?beginDate=' + date
    header={    #请求头部
    	'accept-encoding':'gzip, deflate, br',
        'accept-language':'zh-CN,zh;q=0.9',
        'User-Agent':'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        }
    response = requests.get(url, headers=header)
    json_dict=json.loads(response.text)['data']
    json_dict = json_dict['list']
    result = []
    for i in range(0,len(json_dict)):
    	result.append([json_dict[i]['movieName'],json_dict[i]['releaseInfo'],json_dict[i]['sumBoxInfo'],json_dict[i]['boxInfo']])
    # 上映天数releaseInfo 总票房sumBoxInfo 当天综合boxInfo movieName
    # print(result[0])
    return result

# 直方图
def histogram(s,num,title,xtitle,ytitle):
	max_num = num
	name = []
	for i in range(0,max_num):
		frequency = s[i]
		name.append(float(frequency[3]))
	print(name)
	# 对结果进行可视化
	hist = pygal.Bar()
	hist.x_labels = [s[j][0] for j in range(0,max_num)]
	hist.x_title = xtitle
	hist.y_title = ytitle

	hist.add(title,name)
	hist.render_to_file('test.svg')

def main():
	url = 'https://box.maoyan.com/promovie/api/box/second.json'
	result = get_day(url,'20180811')
	histogram(result,10,'2018-08-11','影片','总票房&综合票房')


if __name__ == '__main__':
	main()



