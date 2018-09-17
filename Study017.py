'''https://fanyi.baidu.com/sug'''
from urllib import request, parse
import json
baseurl = 'https://fanyi.baidu.com/sug'
value = input("请输入你想查译的单词：")
data = {"kw":value}
data = parse.urlencode(data).encode("utf-8")
print(data)
headers = {
    'Content-Length': len(data)
}
print(headers)
rsp = request.urlopen(baseurl, data = data)
print(rsp)
json_data = rsp.read().decode()
print(json_data)
json_data = json.loads(json_data)
print(json_data)
for item in json_data['data']:
    print(item['v'])
