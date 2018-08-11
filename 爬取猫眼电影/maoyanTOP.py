import requests
import re
import csv

# 爬取猫眼 TOP100 榜

def get_page(url,page=0):
	url = url + '?offset=' + str(page*10)
	header={    #请求头部
        'User-Agent':'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
	response = requests.get(url, headers=header)
	html = response.text

	pat_index = r'<i class="board-index.*?">(.*?)</i>'
	pat_img = r'<img data-src="(.*?)@160w_220h_1e_1c" .* />'
	pat_src_title = r'<a href="(.*?)" title=.*>(.*?)</a>'
	pat_star_time = r'<p class="star">\n *主演：(.*?)\n.*</p>\n<p class="releasetime">上映时间：(.*)</p>'
	result_index = re.compile(pat_index).findall(html)
	result_img = re.compile(pat_img).findall(html)
	result_src_title = re.compile(pat_src_title).findall(html)
	result_star_time = re.compile(pat_star_time).findall(html)

	movie = []
	for i in range(0,len(result_index)):
		item = {
			'index':result_index[i],
			'title':result_src_title[i][1],
			'star':result_star_time[i][0],
			'releasetime':result_star_time[i][1],
			'src':result_src_title[i][0],
			'img':result_img[i]}
		movie.append(item)

	if response.status_code == 200:
		return movie
	return None

def do_file(movie):
	with open('猫眼TOP100.csv','w+') as file:
		writer = csv.writer(file)
		writer.writerow(['排名','影片名','','参演演员','','','','上映时间','','','影片路径','','封面'])
		for item in movie:
			for line in item:
				writer.writerow([line['index'],line['title'],'',line['star'],'','','',line['releasetime'],'','',line['src'],'',line['img']])



def main():
	movie = []
	url = 'http://maoyan.com/board/4'
	for i in range(0,10):
		movie.append(get_page(url,i))
	do_file(movie)


if __name__ == '__main__':
	main()