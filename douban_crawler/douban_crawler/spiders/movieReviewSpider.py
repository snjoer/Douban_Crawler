'''

This spider extracts review content from the given link of "review_links" 
which can be accessed from Redis Database by redis_key: "review_links" 
and stores the content to HBase Database.

'''

import scrapy
from scrapy_redis.spiders import RedisSpider

class MovieReviewSpider(RedisSpider):
    name = "review"
    redis_key = "review_links"

    def parse(self, response):
        # todo
        pass
