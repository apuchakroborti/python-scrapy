import scrapy
from ..items import QuotetutorialItem

class QuoteSpider(scrapy.Spider):
	name='quotes'
	start_urls=[
		'http://quotes.toscrape.com/'
	]

	def parse(self, response):

		items = QuotetutorialItem()
		#this is for title, author and tags extracttion
		all_div_quotes =response.css('div.quote')

		for quotes in all_div_quotes:
			title = quotes.css('span.text::text').extract()
			author = quotes.css('.author::text').extract()
			tag = quotes.css('.tag::text').extract()

			items['title'] = title
			items['author'] = author
			items['tag'] = tag

			#yield{
			#	'title': title,
			#	'author': author,
			#	'tag': tag
			#}
			#alternative
			yield items

		#this is for simple titile textb extraction
		#title = response.css('title::text').extract()
		#yield{'titletext':title}
