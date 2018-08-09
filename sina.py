import requests,re,threading
def sina():
	ii=0 #从第一页开始
	while ii<10:
		ii=ii+1
		threading.Thread(target=weibo,args=(ii,)).start()
def weibo(ii):
	url='https://m.weibo.cn/api/comments/show?id=4266867814030917&page='+str(ii) 
	html=requests.get(url)
	# try:
	for jj in range(0,len(html.json()['data']['data'])):
		data=html.json()['data']['data'][jj]['text']
			#打开文件'[\u4e00-\u9fa5]'
		with open('C:\\Users\\soft\\Desktop\\other\\python\\weibo.txt',"a") as ff:
			hanzi = ''.join(re.findall('[\u4e00-\u9fa5]',data)) #提取汉字
			ff.write(hanzi+'\n')
	# except e:
	# 	print(e)

sina()