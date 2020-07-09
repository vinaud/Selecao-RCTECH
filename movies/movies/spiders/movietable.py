import scrapy


class MovietableSpider(scrapy.Spider):
    name = 'movietable'
    allowed_domains = ['pastebin.com']
    start_urls = ['https://pastebin.com/PcVfQ1ff/']

    def parse(self, response):
        all_movies = response.xpath('//tbody')

        for movie in all_movies:
            genero = movie.xpath('.//tr/td/').extract_first()
           
            print(genero)
        

        print('Response status:', response.status)
        print(response.txt)
