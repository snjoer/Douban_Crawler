'''

This spider extracts review content from the given link of "review_links" 
which can be accessed from Redis Data base by redis_key: "review_links" 
and stores the content to HBase Database.

'''

import scrapy
from scrapy.redis.spider import RedisSpider

class MovieReviewSpider(RedisSpider):
    name = "reviewLinks"
    redis_key = "review_links"

    def parse(self, response):
        # todo
        pass
