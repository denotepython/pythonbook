# -*- coding: utf-8 -*-
import urllib2 
import random
url = "http://blog.csdn.net/raylee2007"
my_headers = [
				"Mozilla/5.0 (Windows NT 10.0; rv:46.0) Gecko/20100101 Firefox/46.0",
				"Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Version/3.1 Safari/525.13",
				"Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13 ",
				"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.12) Gecko/20080219 Firefox/2.0.0.12 Navigator/9.0.0.6",
				"Mozilla/5.0 (Macintosh; PPC Mac OS X; U; en) Opera 8.0",
				"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)",
				"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.2)",
				"Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1"	
			]

def get_content(url,headers):
	'''
	@获取403禁止访问的网页
	'''
	random_header = random.choice(headers)
	print random_header
	req = urllib2.Request(url)
	req.add_header("User-Agent", random_header)
	req.add_header("Host", "blog.csdn.net")
	req.add_header("Referer", "http://blog.csdn.net/experts.html")
	req.add_header("GET", url)

	html = urllib2.urlopen(req)
	content = html.read()
	info = html.info()
	return content

print get_content(url,my_headers)