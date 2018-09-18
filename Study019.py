from urllib import request, error, parse
if __name__ == '__main__':
    url = "http://www.baidu.com"
    try:
        req = request.Request(url)
        req.add_header("User-Agent", "Mozilla/5.0 (iPhone; U; CPU like Mac OS X; en) AppleWebKit/420+ (KHTML, like Gecko) Version/3.0 Mobile/1C28 Safari/419.3")
        rsp = request.urlopen(req)
        html = rsp.read().decode()