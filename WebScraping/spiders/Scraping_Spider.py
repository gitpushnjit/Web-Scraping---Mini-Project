import scrapy
from ..items import WebscrapingItem
class ScrapingSpider(scrapy.Spider):
    name='scrape'
    pageNum=2
    start_urls=[
        'http://quotes.toscrape.com/page/1/'
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

        nextPage='http://quotes.toscrape.com/page/'+str(ScrapingSpider.pageNum)+'/'


        if ScrapingSpider.pageNum<11:
            ScrapingSpider.pageNum+=1
            yield response.follow(nextPage, callback=self.parse)

