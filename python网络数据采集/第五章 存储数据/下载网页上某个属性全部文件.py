from urllib import urlopen, urlretrieve
from bs4 import BeautifulSoup
import os

downloadDirectory = 'downloaded'
baseurl = "http://pythonscraping.com"

def get_absoluteurl(baseurl, source):
	if source.startswith("http://www."):
		url = "http://" + source[11:]
	elif source.startswith("http://"):
		url = source
	elif source.startswith("www."):
		url = source[4:]
		url = "http://" + url
	else:
		url = baseurl + "/" + source
	if baseurl not in url:
		return None
	return url 

def getdownloadpath(baseurl, absoluteurl, downloadDirectory):
	path = absoluteurl.replace("www.", "")
	path = path.replace(baseurl, "")
	path = downloadDirectory + path
	dictory = os.path.dirname(path)
	if not os.path.exists(dictory):
		os.makedirs(dictory)
	return path

html = urlopen("http://pythonscraping.com")
bs_obj = BeautifulSoup(html)
downloadlist = bs_obj.findAll(src = True)

for download in downloadlist:
	fileurl = get_absoluteurl(baseurl, download["src"])
	if fileurl is not None:
		print fileurl

urlretrieve(fileurl, getdownloadpath(baseurl, fileurl, downloadDirectory))

	