from scrapy.seletor import Seletor
from scrapy import Spider
from wikiSpider.items import Article

class ArticleSpider(Spider):
	name = "article"
	allowed_domins = ["en.wikipedia.org"]
	start_url = ["http://en.wikipedia.org/wiki/Main_Page", "http://en.wikipedia.org/wiki/Python_%28programming_language%29"]
	def parse(self, response):
		item = Article()
		title = response.xpath('//h1/text()')[0].extact()
		print "Title is:" + title
		item['title'] = title
		return item