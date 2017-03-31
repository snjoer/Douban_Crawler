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
    name = "reviewLinks"
    redis_key = "more_reviews"

    def parse(self, response):
        lists = response.xpath('//div[@class="main review_item"]')

        for li in lists:
            link=li.xpath('.//header[@class="main-hd"]/h3[@class="title"]/a/@herf').extract()
        print link

           # os.system(redis-cli lpush more_reviews_link link)


