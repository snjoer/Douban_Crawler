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

class BookReviewLinksSpider(RedisSpider):
    name = "reviewLinks"
    redis_key = "more_reviews"

    def parse(self, response):
        #todo
        pass
