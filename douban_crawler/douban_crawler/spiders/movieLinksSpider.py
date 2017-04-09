'''

This spider crawls iterates index pages and then release movie links 
to Redis Database with redis_key: "movie_links"

'''    
import os
import scrapy

class DoubanMovieSpider(scrapy.Spider):
    name = "movieLinks"
    start_urls = ["https://movie.douban.com/tag/2016",]

    def parse(self, response):
        host = self.settings['REDIS_HOST']

        lists = response.xpath('//div[@class="pl2"]/a/@href').extract()
        for li in lists:
            command = "redis-cli -h " + host + " lpush movie_links " + li
            os.system(command)

            url = response.xpath('//span[@class="next"]/a/@href').extract()[0]
            yield scrapy.Request(url, callback=self.parse)
