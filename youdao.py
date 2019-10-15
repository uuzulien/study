import requests
import time
import random
import hashlib

def get_md5(string):
    string = string.encode('utf-8')
    md5 = hashlib.md5(string).hexdigest()
    return md5

def translates():
    context = input('请输入要翻译的内容：')
    ts = str(int(time.time()*1000))
    salt = ts + str(random.randint(0, 9))
    bv = get_md5("5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36")
    sign = get_md5("fanyideskweb" + context + salt + "n%A-rKaT5fb[Gy?;N5@Tj")
    data = {
        'i' : context,
        'form' : 'AUTO',
        'to' : 'AUTO',
        'smartresult' : 'dict',
        'client' : 'fanyideskweb',
        'salt' : salt,
        'sign': sign,
        'ts' : ts,
        'bv' : bv,
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_CLICKBUTTION'
    }
    r = requests.post(url=url,data=data,headers=headers,cookies=cookies)
    content = r.json()
    print(content['translateResult'][0][0]['tgt'])

if __name__ == '__main__':
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    cookies = {'OUTFOX_SEARCH_USER_ID':'1653480669@101.169.1.84'}
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36','Referer': 'http://fanyi.youdao.com/'}
    translates()