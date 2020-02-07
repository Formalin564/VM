# -*- coding: utf-8 -*-
import urllib.parse
import urllib.request
import json

key = 'iq9mhXfEXPYMlLyn070A3uvFFx968kpq'

#属性名1：x 用于存储经度 类型 float
#属性名2：y 用于存储纬度 类型 float

#逆地址编码的方法

class locationXY:
    def __init__(self,x,y):
        self.x=x
        self.y=y

#正/逆地理编码
def getLocation(address):

    data = urllib.parse.urlencode({'address': address, 'output': 'json','ak':key})
    response = urllib.request.urlopen('http://api.map.baidu.com/geocoding/v3/?%s' % data)
    html = response.read()
    data = html.decode('utf-8')
    result=json.loads(data)
    
    if result['status'] == 0 :
        lng = result['result']['location']['lng']  # 纬度
        lat = result['result']['location']['lat']  # 经度
        l=locationXY(lng,lat)
        return l

    else:
        print(address+"没找到")