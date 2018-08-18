import json
from Crypto.Cipher import AES  #新的加密模块只接受bytes数据，否者报错，密匙明文什么的要先转码
import base64
import binascii
import random

pub_key ="010001"#第二参数，rsa公匙组成
modulus = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
#第三参数，rsa公匙组成
secret_key = b'0CoJUm6Qyw8W8jud'#第四参数，aes密匙


#生成随机长度为16的字符串的二进制编码
def random_16():
    return bytes(''.join(random.sample('1234567890DeepDarkFantasy',16)),'utf-8')


#aes加密
def aes_encrypt(text,key):
    pad = 16 - len(text)%16 #对长度不是16倍数的字符串进行补全，然后在转为bytes数据
    try:                    #如果接到bytes数据（如第一次aes加密得到的密文）要解码再进行补全
        text = text.decode()
    except:
        pass
    text = text + pad * chr(pad)
    try:
        text = text.encode()
    except:
        pass
    encryptor = AES.new(key,AES.MODE_CBC,b'0102030405060708')
    ciphertext = encryptor.encrypt(text)
    ciphertext = base64.b64encode(ciphertext)#得到的密文还要进行base64编码
    return ciphertext

#rsa加密
def rsa_encrypt(ran_16,pub_key,modulus):
    text = ran_16[::-1]#明文处理，反序并hex编码
    rsa = int(binascii.hexlify(text), 16) ** int(pub_key, 16) % int(modulus, 16)
    return format(rsa, 'x').zfill(256)

#返回加密后内容
def encrypt_data(data):#接收第一参数，传个字典进去
    ran_16 = random_16()
    text = json.dumps(data)
    params = aes_encrypt(text,secret_key)#两次aes加密
    params = aes_encrypt(params,ran_16)
    encSecKey = rsa_encrypt(ran_16,pub_key,modulus)
    return  {'params':params.decode(),
             'encSecKey':encSecKey  }

def encrypt(id,page):
    total = "true"
    if page > 1:
        total = "false"
    data = {'rid': "R_SO_4_"+id, 'offset': (page-1)*20, 'total': total, 'limit': "20", 'csrf_token': "f15b016ca1e43812f78a260998917527"}
    FormData = encrypt_data(data)
    # print(data)
    return FormData


if __name__ == '__main__':
    encrypt('32408691',1)
    encrypt('32408691',2)
    encrypt('32408691',3)