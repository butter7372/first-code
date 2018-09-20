from urllib import request, parse
from http import cookiejar
#创建cookiejar的实例
cookie = cookiejar.CookieJar()
#生成cookie的管理器
cookie_handler = request.HTTPCookieProcessor(cookie)
#创建http请求管理器
http_handler = request.HTTPHandler
#生成https管理器
https_handler = request.HTTPSHandler
#创建请求管理器
opener = request.build_opener(http_handler,https_handler,cookie_handler)
def login():
    """
    负责初次登录
    需要输入用户名和密码 --- 用来获取登录的cookie凭证
    :return:
    """
#此url需要从登录form的action属性中提取
    url = 'http://www.renren.com/PLogin.do'
    data = {
        "email": "18604112626",
        "password": "niuniu1314"
    }
#把数据进行编码
    data = parse.urlencode(data)
#创建一个请求对象
    req = request.Request(url, data = data.encode())
#使用opener发出请求
    rsp = opener.open(req)
def getHomePage():
    url = "http://www.renren.com/968106565"
#如果已执行了login登录，则opener自动已经包含对应的cookie值
    rsp = opener.open(url)
    html = rsp.read().decode()
    with open("rsp.html", "w") as f:
        f.write(html)
if __name__ == '__main__':
     login()
     getHomePage()

