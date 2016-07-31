# -*- coding: utf-8 -*-
import urllib2 #相比urllib更加强大，可以设置代理IP，模仿用户行为
url = "http://blog.csdn.net/raylee2007"
my_headers = {
			"Host": "blog.csdn.net",
			"Referer":	"http://blog.csdn.net/experts.html",
			"User-Agent":"Mozilla/5.0 (Windows NT 10.0; rv:46.0) Gecko/20100101 Firefox/46.0",
			"GET":url
			}
req = urllib2.Request(url, headers = my_headers) #创建一个request对象
# req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:46.0) Gecko/20100101 Firefox/46.0")
# req.add_header("GET", url)
# req.add_header("Host", "blog.csdn.net")
# req.add_header("Referer", "http://blog.csdn.net/experts.html")
html = urllib2.urlopen(req)

print html.read()