def readAll(url):
	with open(url,'r+',encoding='gb18030') as file_object:
		contents = file_object.read()
		# print(contents)
		return contents

def readline():
	with open('xx.txt','r+',encoding='gb18030') as file_object:
		for line in file_object:
			print(line.rstrip())

def cal():
	a = input('输入一个数字')
	if a == 'q':
		return
	b = input('输入一个数字')
	try:
		answer = int(a)/int(b)
	except ZeroDivisionError:
		print('error')
	else:
		print(answer)

def test():
	s = 'hello good boy doiido' 
	print(s.startswith('h'))
	print(s.split())
	print(s.lower().count('o'))
	s = readAll('./other/西游记.txt')
	print(len(s))

def Statistics(url):
	s = readAll(url)
	table = str.maketrans('，。；！？（）：“”、,.!?\n','                ',' ')
	s = s.translate(table)
	s = s.translate(table)
	d = {}
	for x in s:
		d[x] = d.get(x,0) +1
	# print(sorted(d.items(),key=lambda x:x[1],reverse=True))
	return sorted(d.items(),key=lambda x:x[1],reverse=True)


# readline()
# Statistics()
if __name__ == '__main__':
	test()
