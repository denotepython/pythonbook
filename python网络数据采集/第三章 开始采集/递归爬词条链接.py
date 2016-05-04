from urllib2 import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now())
#初始化随机数发生器
def getlink(article_url):
	url = "http://en.wikipedia.org" + article_url
	html = urlopen(url)
	bs_obj = BeautifulSoup(html)
	link = bs_obj.find("div", id = "bodyContent").findAll("a", href = re.compile("^(/wiki/)((?!:).)*$"))
	return link

links = getlink("/wiki/Kevin_Bacon")
while len(links) > 0:
	newarticle = links[random.randint(0, len(links) - 1)].attrs["href"]
	print(newarticle)
	links = getlink(newarticle)

#从打印速度上也看得出执行得非常缓慢