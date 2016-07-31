from urllib import urlretrieve
from urllib import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com")
bs_obj = BeautifulSoup(html)
image_loction = bs_obj.find("a", id = "logo").find("img")['src']
urlretrieve(image_loction, "logo.jpg")