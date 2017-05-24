'''

This spider extracts review links from the given link of "more reviews" 
which can be accessed from Redis Database by redis_key: "more_reviews" 
and stores link to every review to Redis Database and the redis_key for 
those links is "review_links".

'''

import scrapy
import logging
from scrapy_redis.spiders import RedisSpider
import os

class MovieReviewLinksSpider(RedisSpider):
    name = "reviewLinks"
    redis_key = "more_reviews"

    def parse(self, response):
        host = self.settings['REDIS_HOST']
        lists = response.xpath('//a[@class="title-link"]/@href')
        
        for li in lists:
            command = "redis-cli -h " + host + " lpush review_links " \
                    + li.extract()
            os.system(command)
        try:
            next_page = response.xpath('//span[@class="next"]/a/@href').extract()[0]
        except IndexError:
            logging.log(logging.INFO, '*** finished crawling ... ')
            return
        url = response.urljoin(next_page)
        #crawl all pages.
        yield scrapy.Request(url, callback=self.parse)
    
