from urllib2 import urlopen
from bs4 import BeautifulSoup
import re

url = "http://en.wikipedia.org/wiki/Kevin_Bacon"
html = urlopen(url)
bs_obj = BeautifulSoup(html)

for link in bs_obj.find("div", {"id": "bodyContent"}).findAll("a", href = re.compile("^(/wiki/)((?!:).)*$")):
	#这一句不是很懂，find和findAll不是并列关系么，为什么是包含关系了，bodyContent也不明白
	if "href" in link.attrs:
		print link.attrs['href']