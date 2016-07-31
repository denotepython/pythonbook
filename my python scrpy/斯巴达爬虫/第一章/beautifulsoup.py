# -*-coding: utf-8 -*-
#爬取下载图片
import urllib
from bs4 import BeautifulSoup
def get_soup(url):
	'''return a BeautifulSoup object'''
	html = urllib.urlopen(url)
	soup = BeautifulSoup(html)
	return soup

def get_images(soup):
	'''doc
	<img class="BDE_Image" src="http://imgsrc.baidu.com/forum/
	'''
	images = soup.findAll("img", class_="BDE_Image")
	count = 0
	for image in images:
		print image
		urllib.urlretrieve(image['src'], "E:\\spider download\\%s.jpg" % count)
		#这里传入的参数不能是image
		count += 1

url = "http://tieba.baidu.com/p/4435196076?pid=88755980874&cid=89244484263#89244484263"
soup = get_soup(url)
print get_images(soup)

