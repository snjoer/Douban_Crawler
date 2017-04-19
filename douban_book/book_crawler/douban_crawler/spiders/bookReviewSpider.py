'''

This spider extracts review content from the given link of "review_links" 
which can be accessed from Redis Database by redis_key: "review_links" 
and stores the content to HBase Database.

'''

import re
import scrapy
from scrapy_redis.spiders import RedisSpider
from douban_crawler.items import ReviewItem

class BookReviewSpider(RedisSpider):
    name = "review"
    redis_key = "review_links"

    def parse(self, response):
        #todo
        pass
