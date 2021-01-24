import urllib.request,urllib.parse,urllib.error

# 获取一个get请求
# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode('utf-8'))

# 获取一个post请求
# data = bytes(urllib.parse.urlencode({"username" : "tomas"}), encoding = "utf-8")
# response = urllib.request.urlopen("http://httpbin.org/post",data = data)
# print(response.read().decode("utf-8"))

# 超时处理
# try:
#    response = urllib.request.urlopen("http://httpbin.org/get",timeout= 0.1)
#    print(response.read().decode("utf-8"))
# except urllib.error.URLError as e:
#     print(e,'time out!!!')

# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.getheaders())

# 封装header
# url = "http://httpbin.org/post"
# data = bytes(urllib.parse.urlencode({"username" : "tomas"}), encoding = "utf-8")
# headers = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
# }
# method = "POST"
# request = urllib.request.Request(url = url, data=data,headers= headers,method = method)
# response = urllib.request.urlopen(request)
# print(response.read().decode("utf-8"))

url = "https://www.douban.com"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}
request = urllib.request.Request(url = url, headers= headers)
response = urllib.request.urlopen(request)
print(response.read().decode("utf-8"))