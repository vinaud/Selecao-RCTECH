import scrapy


class MovietableSpider(scrapy.Spider):
    name = 'movietable'
    allowed_domains = ['pastebin.com']
    start_urls = ['https://pastebin.com/PcVfQ1ff/', 'https://pastebin.com/Tdp532rr']

    def parse(self, response):
        print(response.status)
