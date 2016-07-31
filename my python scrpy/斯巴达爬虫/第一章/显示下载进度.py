#-*-coding: utf-8 -*-

import urllib
import turtle
def callback(a,b,c):
	'''
	a.到目前为止传递的数据块数量
	b.每个数据块的大小，单位为字节
	c.远程文件大小,在头部信息里面可查看
	'''
	download_percent = 100 * a *b / c
	if download_percent > 100:
		download_percent = 100
	print "%.2f%%" % download_percent,
	#加一个逗号就可以在一行显示


url = "http://www.python.org"
local = "E:\\spider download\\python.html"
# print html.info()
urllib.urlretrieve(url, local, callback)
