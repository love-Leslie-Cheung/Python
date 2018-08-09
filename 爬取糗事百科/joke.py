# -*- coding:utf-8 -*-
import re
import urllib.request
import urllib.error
import urllib.parse
import time

page = 1
head = ['Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)'
]

def get_joke_list(page):
    url = 'http://www.qiushibaike.com/hot/page/' + str(page)
    header={    #请求头部
        'User-Agent':'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    request=urllib.request.Request(url=url, headers=header)
    html=urllib.request.urlopen(request).read().decode('utf8')
    # print(html)
    pat_id = r'<a href="/article/(\d*)" target="_blank" class="contentHerf"'
    result_id = re.compile(pat_id).findall(html)
    return result_id


def get_joke(id,head):
    url = 'https://www.qiushibaike.com/article/' + id
    header={    #请求头部
        'User-Agent':head #'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    request=urllib.request.Request(url=url, headers=header)
    html=urllib.request.urlopen(request).read().decode('utf8')
    # print(html)
    pat_autor = r'<h2>(.*?)</h2>'
    pat_content = r'<div class="content">\n*?(.*?)\n*?</div>'
    pat_img = r'<div class="thumb">\n*?(.*?)\n*?</div>'
    result1 = re.compile(pat_autor).findall(html)
    result2 = re.compile(pat_content).findall(html)
    result3 = re.compile(pat_img).findall(html)
    if result3:
        pass
    else :
        print(result1[0] + '\n' + result2[0].replace('<br/>','\n') + '\n')


id = get_joke_list(page)
for i in range(0,len(id)):
    get_joke(id[i],head[i%8])
    if i%5 == 0:
        time.sleep(0.5)