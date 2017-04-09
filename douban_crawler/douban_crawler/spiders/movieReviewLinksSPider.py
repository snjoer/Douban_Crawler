'''

This spider extracts review links from the given link of "more reviews" 
which can be accessed from Redis Database by redis_key: "more_reviews" 
and stores link to every review to Redis Database and the redis_key for 
those links is "review_links".

'''

import scrapy
from scrapy_redis.spiders import RedisSpider
import os

class MovieReviewLinksSpider(RedisSpider):
    count = 0
    total = 0
    url = ""
    name = "reviewLinks"
    redis_key = "more_reviews"

    def parse(self, response):
        host = self.settings['REDIS_HOST']
        lists = response.xpath('//a[@class="title-link"]/@href')
        
        for li in lists:
            command = "redis-cli -h" + host + " lpush review_links " \
                    + li.extract()
            os.system(command)
        
        if self.count == 0:
            num = response.xpath('//span[@class="thispage"]/@data-total-page').extract()[0]
            num = int(num)
            self.url = response.url
            self.total = num * 20
        self.count += 20 
        # crawl all pages.
        if self.count < self.total:
            new_url = self.url + '?start=' + str(self.count)
            yield scrapy.Request(new_url, callback=self.parse)
        # reset count when all pages have been crawled.
        else:
            self.count = 0
