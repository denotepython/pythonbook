# -*-coding: utf-8 -*-
import urllib
url = "http://www.163.com"
html = urllib.urlopen(url)

#html.read().decode("gbk","ignore").encode("utf-8")
#print html.info()
#urllib.urlretrieve(url, "E:\\web.html")
'''
第一个参数：是传入的网址
第二个参数：是路径+文件名 
	文件保存路径不能含有中文
	\\需要转义
第三个参数：函数调用，该函数行为可以自定义，参数必须三个
	1.到目前为止传递的数据块数量
	2.每个数据块的大小，单位为字节
	3.远程文件大小
html.close()
'''
'''
html.getcode() 获取网页状态码
网页状态码 200正常。301重定向，404网页不存在，403禁止访问 
'''
#快速多行注释，用ctrl+/
#ctrl + z 撤销上一步操作——前进
#ctrl + shift + z 恢复上一步操作——前进
#ctrl + y 重复上一步操作——前进