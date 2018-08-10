import requests,re,threading,time

# 只能抓取部分评论，否则ip暂时被封
def sina():
	ii=1 #从第一页开始
	while ii<500:
		if i%10 == 0:
			time.sleep(1.2)
		else:
			time.sleep(0.8)
		weibo(ii)
		ii=ii+1
def weibo(ii):
	global i
	url='https://m.weibo.cn/api/comments/show?id=4271165482609880&page='+str(ii) 
	header={    #请求头部
        'User-Agent':'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
	html=requests.get(url,headers=header)
	# try:
	for jj in range(0,len(html.json()['data']['data'])):
		data=html.json()['data']['data'][jj]['text']
			#打开文件'[\u4e00-\u9fa5]'
		with open('C:\\Users\\soft\\Desktop\\weibo.txt',"a") as ff:
			hanzi = ''.join(re.findall('[\u4e00-\u9fa5]',data)) #提取汉字
			ff.write(hanzi+'\n')
			i = i + 1
			print(i)




if __name__ == '__main__':
	i = 0
	sina()