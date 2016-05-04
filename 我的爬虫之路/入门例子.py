import urllib, urllib2, cookielib

#爬一个网页
'''
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  
headers = { 'User-Agent' : user_agent } 
user = {"username":"123456@qq.com", "password":"*********"} #账号密码存储为字典格式
data = urllib.urlencode(user)
url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request = urllib2.Request(url, data, headers) #data用来传入账户密码
response = urllib2.urlopen(request)
# urlopen(url, data, timeout)三个参数。data是访问url时需要传入的参数，timeout为超时时间
print response.read()
'''


#获取cookie保存
'''
filename = 'cookie.txt'
cookie = cookielib.MozillaCookieJar(filename) #声明一个coookie.jar对象实例来保存ciikie
handler = urllib2.HTTPCookieProcessor(cookie) #利用HTTPCookieProcessor创建一个cookie处理器
opener = urllib2.build_opener(handler) #构建一个opener，比自带的open强大
response = opener.open('http://www.baidu.com')
for item in cookie:
	print 'Name = ' + item.name
	print 'Value = ' + item.value
'''
'''
cookie.save(ignore_discard = True, ignore_expires = True) 
这句保存文件到本地,ignore_discard的意思是即使cookies将被丢弃也将它保存下来，
ignore_expires的意思是如果在该文件中cookies已经存在，则覆盖原文件写入
'''
#利用cookie去访问网页
filename = 'HUBcookie.txt'
cookie = cookielib.MozillaCookieJar(filename)
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
user = {'stu' : 'U201213921', 'password' : 'LIUDAORUO1994'}
data = urllib.urlencode(user)
url = 'http://hub.hust.edu.cn/index.jsp'
result = opener.open(url, data)
cookie.save(ignore_discard = True, ignore_expires = True)
scoreurl = 'http://s.hub.hust.edu.cn/aam/score/QueryScoreByStudent_readyToQuery.action'
result = opener.open(scoreurl)
print result.read()

