# -*- coding:utf-8 -*-
from urllib2 import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
allinterlinks = set()
allexterlinks = set()
random.seed(datetime.datetime.now())

def getinterlinks(bs_obj, interurl):
	interlinks = []
	for link in bs_obj.findAll("a", href = re.compile("^(/|.*"+interurl+")")):
		if link.attrs['href'] is not None:
			if link.attrs['href'] not in interlinks:
				interlinks.append(link.attrs['href'])
	return interlinks

def getexterlinks(bs_obj, exterurl):
	exterlinks = []
	for link in bs_obj.findAll("a", href = re.compile("^(http|www)((?!"+exterurl+").)*$")):
		if link.attrs['href'] is not None:
			if link.attrs['href'] not in exterlinks:
				exterlinks.append(link.attrs['href'])
	return exterlinks

def splitadd(address):
	addresspart = address.replace("http://", "").split("/")
	return addresspart

'''
def getall_exterlinks(url):
	html = urlopen(url)
	bs_obj = BeautifulSoup(html)
	interlinks = getinterlinks(bs_obj, splitadd(url)[0])
	exterlinks = getexterlinks(bs_obj, splitadd(url)[0])
	for link in exterlinks:
		if link not in allexterlinks:
			allexterlinks.add(link)
			print link
	for link in interlinks:
		if link not in allinterlinks:
			print "即将获取链接的url是" 
			print link
			allinterlinks.add(link)
			getall_exterlinks(link)

getall_exterlinks("http://oreilly.com")
'''

def  getrandom_exterlinks(starturl):
	html = urlopen(starturl)
	bs_obj = BeautifulSoup(html)
	exterlinks = getexterlinks(bs_obj, splitadd(starturl)[0])
	if len(exterlinks) == 0:
		interlinks = getinterlinks(starturl)
		return getnext_exterlink(interlinks[random.randint(0, len(interlinks) - 1)])
	else:
		return exterlinks[random.randint(0, len(exterlinks) - 1)]

def followexterlinks(starturl):
	exterlink = getrandom_exterlinks("http://oreilly.com")
	print "随即外链是：" + exterlink
	followexterlinks(exterlink)

followexterlinks("http://oreilly.com")