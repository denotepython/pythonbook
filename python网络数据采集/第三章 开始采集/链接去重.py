from urllib2 import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
def getlinks(pageurl):
	global pages
	html = urlopen("https://github.com" + pageurl)
	bs_obj = BeautifulSoup(html, "lxml")
	for link in bs_obj.findAll("a", href = re.compile("^/")):
		if 'href' in link.attrs:
			if link.attrs['href'] not in pages:
				newpage = link.attrs['href']
				print(newpage)
				pages.add(newpage)
				getlinks(newpage)

getlinks("")

