import scrapy
from ..items import WebscrapingItem
class ScrapingSpider(scrapy.Spider):
    name='scrape'
    start_urls=[
        'http://quotes.toscrape.com/'
    ]

    def parse(self, response):

        items=WebscrapingItem()
        allDivQuotes= response.css("div.quote")

        for i in allDivQuotes:
            quotes= i.css("span.text::text").extract()
            authors= i.css(".author::text").extract()
            tags= i.css(".tag::text").extract()

            items['quotes']=quotes
            items['authors'] = authors
            items['tags'] = tags

            yield items
         # title=response.css('title::text').extract()
         # yield {'TextTitle':title}
