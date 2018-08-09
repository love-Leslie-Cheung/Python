import re
import urllib.request
import urllib.error
import urllib.parse
import json
import time
import os

def get_book():
    url = 'https://www.qu.la/book/394/296430.html'
    header={    #请求头部
        'User-Agent':'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    request=urllib.request.Request(url=url, headers=header)
    html=urllib.request.urlopen(request).read().decode('utf8')
    html=str(html)
    pat = r'[&nbsp;]{24}(.*?)<br/>'
    result=re.compile(pat).findall(html)
    print(len(result))
    for x in result:
    	print('\t\t\t\t' + x + '\n')
get_book()