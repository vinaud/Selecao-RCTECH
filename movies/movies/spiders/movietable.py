import scrapy


class MovietableSpider(scrapy.Spider):
    name = 'movietable'
    allowed_domains = ['https://pastebin.com/PcVfQ1ff']
    start_urls = ['http://https://pastebin.com/PcVfQ1ff/']

    def parse(self, response):
        pass
