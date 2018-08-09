import re
import urllib.request
import urllib.error
import urllib.parse
import json
import time
import os


# 获取歌单歌曲信息
def get_list_song(list_id):
    url = 'https://music.163.com/playlist?id=' + list_id
    header={    #请求头部
        'User-Agent':'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    request=urllib.request.Request(url=url, headers=header)
    html=urllib.request.urlopen(request).read().decode('utf8')
    pat_list=r'<h2 class="f-ff2 f-brk">(\w*)</h2>'
    pat_author=r'data-res-author="(\w*)"'
    patt_time=r'"pubDate": "(.*)"'
    pat_count=r'<span id="playlist-track-count">(\d*)</span>'
    pat_id = r'<a href="/song\?id=(\d*)">.*?</a>'
    pat_title = r'<a href="/song\?id=\d*">(.*?)</a></li>'
    result1=re.compile(pat_list).findall(html) 
    result2=re.compile(pat_author).findall(html) 
    result3=re.compile(patt_time).findall(html) 
    result4=re.compile(pat_count).findall(html) 
    result_id=re.compile(pat_id).findall(html) 
    result_title=re.compile(pat_title).findall(html) 
    file = open('./'+result1[0]+'.txt','w',encoding='utf-8')
    file.write('歌单名:'+result1[0] + '\t创建者:' + result2[0] + '\t创建时间:' + result3[0] +'\t共'+result4[0] +'首歌')
    file.write('\n================================================\n')
    for item in range(0,len(result_id)):
        file.write('id:' + '{:<20}'.format(str(result_id[item]),) + '\t歌名:' + str(result_title[item]) +'\n')
    file.close()
    return result1[0],result_id,result_title
    

def get_song_name(id):
    url = 'https://music.163.com/song?id='+id
    header={    #请求头部
        'User-Agent':'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    request=urllib.request.Request(url=url, headers=header)
    html=urllib.request.urlopen(request).read().decode('utf8')
    html=str(html)
    pat1=r'<em class="f-ff2">(.*)</em>'  #进行第一次筛选的正则表达式
    result=re.compile(pat1).findall(html)     #用正则表达式进行筛选
    result=result[0]
    return result

# 获取歌曲热评
def get_hotComments(list_path,id,song_name):
    url='http://music.163.com/weapi/v1/resource/comments/R_SO_4_' + id + '?csrf_token='   #歌评url
    header={    #请求头部
   'User-Agent':'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
   }
    #post请求表单数据
    data={'params':'B78zCl17nXvGyj8AY6VzmwUQF+kzD12zj+F6MX7jruwpd33mMeTTuWpt1x4YP85Vd+shMqs0qrqy0sNxJiJOdszxintXdI1ezifUrO5EelBe85DCKgyQmg8TyZCVAgZLYMxRUMIiAibhnwyjv5rGMhaje7DarJoH771Q1ZXxrrzIK9tlDstoeJT6SHA4vZT9','encSecKey':'df0a685d2e2d2866a2f58c0fcbae4ebfd2099cb4daffbce3b47861c471143a7c1697914fec4e11f3cecead45422d16cf422239b561b48f425d3d2f8933e997a522fde18a44a48a7415750aaef5f5ddac2769352b133d54c31d1d70ef7e91b3683680cd30280aad49e50ea1be2c0ba8bc7d8df4f61026c037a6d0a4a56ed86dc0'}
    postdata=urllib.parse.urlencode(data).encode('utf8')  #进行编码
    request=urllib.request.Request(url,headers=header,data=postdata)
    reponse=urllib.request.urlopen(request).read().decode('utf8')
    json_dict=json.loads(reponse)   #获取json
    hot_commit=json_dict['hotComments']  #获取json中的热门评论


    num=0
    fhandle=open(list_path + '/'+song_name+'.txt','w',encoding='utf-8')  #写入文件
    fhandle.write(song_name +':'+'共'+ str(json_dict['total']) +'条评论\n')

    fhandle.write('精彩评论：\n')
    for item in hot_commit:
        num+=1
        st = time.localtime(item['time']/1000)
        fhandle.write(str(num)+'.'+ item['user']['nickname'] +'：\t'+time.strftime('%Y-%m-%d %H:%M:%S', st)+ '(点赞' + str(item['likedCount']) +')\n\t')
        fhandle.write(item['content']+ '\n')
    fhandle.close()

# 获取20条最新评论
def get_Comments(list_path,id,song_name):
    url='http://music.163.com/weapi/v1/resource/comments/R_SO_4_' + id + '?csrf_token='   #歌评url
    header={    #请求头部
   'User-Agent':'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
   }
    #post请求表单数据
    data={'params':'B78zCl17nXvGyj8AY6VzmwUQF+kzD12zj+F6MX7jruwpd33mMeTTuWpt1x4YP85Vd+shMqs0qrqy0sNxJiJOdszxintXdI1ezifUrO5EelBe85DCKgyQmg8TyZCVAgZLYMxRUMIiAibhnwyjv5rGMhaje7DarJoH771Q1ZXxrrzIK9tlDstoeJT6SHA4vZT9','encSecKey':'df0a685d2e2d2866a2f58c0fcbae4ebfd2099cb4daffbce3b47861c471143a7c1697914fec4e11f3cecead45422d16cf422239b561b48f425d3d2f8933e997a522fde18a44a48a7415750aaef5f5ddac2769352b133d54c31d1d70ef7e91b3683680cd30280aad49e50ea1be2c0ba8bc7d8df4f61026c037a6d0a4a56ed86dc0'}
    postdata=urllib.parse.urlencode(data).encode('utf8')  #进行编码
    request=urllib.request.Request(url,headers=header,data=postdata)
    reponse=urllib.request.urlopen(request).read().decode('utf8')
    json_dict=json.loads(reponse)   #获取json
    comment=json_dict['comments']  #获取json中的热门评论


    num=0
    fhandle=open(list_path + '/'+ song_name+'.txt','a',encoding='utf-8')  #写入文件
    fhandle.write('最新评论('+ str(json_dict['total']) +')：\n')
    for item in comment:
        num+=1
        st = time.localtime(item['time']/1000)
        fhandle.write(str(num)+'.'+ item['user']['nickname'] + ': ' +time.strftime('%Y-%m-%d %H:%M:%S', st) +'('+ str(item['likedCount']) +'赞):\n\t')
        fhandle.write(item['content']+'\n')
    fhandle.write('\n==============================================\n\n')
    fhandle.close()


list_path,list_id,list_title = get_list_song('380179013')
list_path = './' + list_path
if not os.path.exists(list_path):
	os.mkdir('./' + list_path)
for i in range(0,len(list_id)):
	try:
		print('正在获取' + list_title[i] + '的热评')
		list_title[i] = list_title[i].replace('/','.')
		# get_hotComments(list_path,list_id[i],list_title[i])
		# get_Comments(list_path,list_id[i],list_title[i])
	except Exception as e:
		print(e)