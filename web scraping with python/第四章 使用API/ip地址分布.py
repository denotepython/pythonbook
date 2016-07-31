from urllib2 import urlopen
from bs4 import BeautifulSoup
import random, re, datetime

random.seed(datetime.datetime.now())
def getlinks(url):
	html = urlopen("http://en.wikipedia.org" + url)
	bs_obj = BeautifulSoup(html)
	return bs_obj.find("div", id = "bodyContent").findAll("a", href = re.compile("^(/wiki/)((?!:).)*$"))

def get_historyip(pageurl):
	pageurl = pageurl.replace("/wiki/", "")
	historyurl = "http://en.wikipedia.org/w/index.php?title=" + pageurl + "&action=history"
	print "history url is:" + historyurl
	html = urlopen(historyurl)
	bs_obj = BeautifulSoup(html)
	ipaddresses = bs_obj.findAll("a", class_ = "mw-anonuserlink")
	addresslist = set()
	for ipaddress in ipaddresses:
		addresslist.add(ipaddress.get_text())
	return addresslist

links = getlinks("/wiki/Python_(programming_language)")

while(len(links) > 0):
	for link in links:
		print "---------------------------------"
		historyips = get_historyip(link.attrs['href'])
		for historyip in historyips:
			print historyip
	newlink = links[random.randint(0, len(links) - 1)].attrs['href']
	links = getlinks(newlink)