'''
This spider crawls iterates index pages and then release movie links 
to Redis Database with redis_key: "movie_links"
'''

import os
import scrapy

class DoubanMovieSpider(scrapy.Spider):
    start_urls = ["https://movie.douban.com/tag/1988",]
    name = "movieLinks"

    def parse(self, response):
        host = self.settings['REDIS_HOST']
        lists = response.xpath('//div[@class="pl2"]/a/@href').extract()
        for li in lists:
            command = "redis-cli -h " + host + " lpush movie_links " + li
            os.system(command)
        try:
            url = response.xpath('//span[@class="next"]/a/@href').extract()[0]
        except:
            return
        yield scrapy.Request(url, callback=self.parse)
