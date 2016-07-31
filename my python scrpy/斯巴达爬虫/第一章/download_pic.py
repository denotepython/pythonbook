# -*-coding: utf-8 -*-
#爬取下载图片
#区分不同图片要用正则表达式
import urllib
import re
def get_content(url):
	'''doc.'''
	html = urllib.urlopen(url)
	content = html.read()
	html.close()
	return content

def get_images(content):
	'''doc
	<img class="BDE_Image" src="http://imgsrc.baidu.com/forum/
	'''
	regex = r'class="BDE_Image" src="(.+?\.jpg)"'
	pattern = re.compile(regex)
	image_urls = re.findall(pattern, content)
	count = 0
	for image_url in image_urls:
		print image_url
		urllib.urlretrieve(image_url, "E:\\spider download\\%s.jpg" % count)
		count += 1

url = "http://tieba.baidu.com/p/4435196076?pid=88755980874&cid=89244484263#89244484263"
content = get_content(url)
print get_images(content)

