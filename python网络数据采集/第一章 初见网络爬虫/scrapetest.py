from urllib2 import urlopen
from bs4 import BeautifulSoup  # not BeautifulSoup4
from urllib2 import HTTPError

def gettitle(url):
	try:
		html = urlopen(url)
	except HTTPError as e:  #检查HTTP错误
		return None
	try:
		bs = BeautifulSoup(html.read(), "lxml")
		title = bs.body.h1
	except AttributeError as e:  #检查BS对象标签错误
		return None 
	return title

title = gettitle("http://www.pythonscraping.com/pages/page1.html")

if title ==  None:
	print "title is not found"
else:
	print title