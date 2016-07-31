from urllib2 import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
def getlinks(pageurl):
	global pages
	html = urlopen("http://en.wikipedia.org" + pageurl)
	bs_obj = BeautifulSoup(html)
	try:
		print bs_obj.h1.get_text()
		print bs_obj.find(id = "mw-content-text").findAll("p")[0]
		print bs_obj.find(id = "ca-edit").find("span").find("a").attrs['href']
	except AttributeError:
		print "页面缺少一些属性"

	for link in bs_obj.findAll("a", href = re.compile("^(/wiki?)")):
		if 'href' in link.attrs:
			if link.attrs['href'] not in pages:
				newpage = link.attrs['href']
				print "---------------------------------\n"
				print newpage
				pages.add(newpage)
				getlinks(newpage)

getlinks("")