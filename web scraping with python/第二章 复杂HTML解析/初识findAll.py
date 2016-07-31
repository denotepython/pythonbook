from urllib2 import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bs_obj = BeautifulSoup(html)
namelist = bs_obj.findAll("span", class_ = "green")
#findAll(tag, attributes, ....) 其中tag是标签参数，attribute是属性参数
for name in namelist:
	print name.get_text() #get_text()会把正在处理的html文档所有超链接，段落，标签清除，
						  #只剩下不带标签的文字，所以一般最后才使用