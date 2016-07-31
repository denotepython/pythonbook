# -*-coding: utf-8 -*-
import urllib
import chardet #字符集检测
def chardetect(url):
	'''
	自动检测网页的编码类型
	'''
	html = urllib.urlopen(url)
	content = html.read()
	result = chardet.detect(content) #参数可以是字符串
	encoding = result['encoding']
	return encoding


urls = ["http://www.163.com","http://jd.com","http://taobao.com"]

for url in urls:
	print url, chardetect(url)

#print info.getparam("charset")
#通过服务器头部获得的编码，可能为none

  
