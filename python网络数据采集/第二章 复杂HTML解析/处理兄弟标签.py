from urllib2 import urlopen
from bs4 import BeautifulSoup

url = "http://www.pythonscraping.com/pages/page3.html"
html = urlopen(url)
bs_obj = BeautifulSoup(html)
htmllist = bs_obj.find("table", id = "giftList").tr.next_siblings

for slibing in htmllist:
	print slibing