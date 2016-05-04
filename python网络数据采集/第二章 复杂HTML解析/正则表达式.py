from urllib2 import urlopen
from bs4 import BeautifulSoup
import re

url = "http://www.pythonscraping.com/pages/page3.html"
html = urlopen(url)
bs_obj = BeautifulSoup(html, "lxml")
images = bs_obj.findAll("img", {"src": re.compile("\.\.\/img\/gifts/img.*\.jpg")})
for image in images:
	print image["src"]