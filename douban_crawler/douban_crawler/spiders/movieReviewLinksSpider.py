'''

This spider extracts review links from the given link of "more reviews" 
which can be accessed from Redis Data base by redis_key: "more_reviews" 
and store link to every review to Redis Database and the redis_key for 
those links is "review_links".

'''

import scrapy
from scrapy.redis.spider import RedisSpider

class MovieReviewLinksSpider(RedisSpider):
    name = "reviewLinks"
    redis_key = "more_reviews"

    def parse(self, response):
        # todo
        pass
