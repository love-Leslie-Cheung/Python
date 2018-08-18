import requests
from bs4 import BeautifulSoup

def my_bs4(url,page):
	url = url + '?offset=' + str(page*10)
	header={    #请求头部
        'User-Agent':'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
	response = requests.get(url, headers=header)
	html = response.text
	# print(html)
	soup = BeautifulSoup(html, 'lxml')
	name = soup.find_all(name='p',attrs={'class': 'name'})
	score = soup.find_all(name='p',class_='score')
	star = soup.find_all(name='p',class_='star')
	time = soup.find_all(name='p',class_='releasetime')
	for i in range(0,len(name)):
		print('{:<20}'.format(name[i].contents[0].string) + '\t' + score[i].text + '\t\t' + star[i].text.strip() + '\t' + time[i].string)

	# for i in soup.find_all(name='p',attrs={'class': 'name'}):
		# print(i.contents[0].string.strip())
	# for j in soup.find_all(name='p',class_='score'):
	# 	print(j.text)
	# for m in soup.find_all(name='p',class_='star'):
	# 	print(m.text.strip())
	# for n in soup.find_all(name='p',class_='releasetime'):
	# 	print(n.string)




def main():
	url = 'http://maoyan.com/board/4'
	my_bs4(url,0)


if __name__ == '__main__':
	main()