'''
This spider crawls iterates index pages and then release movie links 
to Redis Database with redis_key: "movie_links"
'''
import scrapy
import os
import random
import string

class DoubanMovieSpider(scrapy.Spider):
    start_urls = ["https://movie.douban.com/tag/1988",]
    name = "movieLinks"

    def parse(self, response):
        if 'https://movie.douban.com/tag/1988?start=20' in response.url:
            return
        host = self.settings['REDIS_HOST']
        lists = response.xpath('//div[@class="pl2"]/a/@href').extract()
        for li in lists:
            command = "redis-cli -h " + host + " lpush movie_links " + li
            os.system(command)
            try:
                url = response.xpath('//span[@class="next"]/a/@href').extract()[0]
            except:
                return
            Cookies = {'Cookie' : 'bid=%s' % ''.join(random.sample(string.ascii_letters + string.digits, 11))}
            yield scrapy.Request(url, callback=self.parse)
