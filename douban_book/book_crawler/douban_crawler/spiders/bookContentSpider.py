'''

This spider extracts specific content from given book links which can be 
accessed from Redis Database by redis_key "book_links" and stores the data
to HBase.
Moreover, this spider should export link to more reviews to Redis Database
as redis_key "more_reviews".

'''
import re,os
from scrapy_redis.spiders import RedisSpider
from douban_crawler.items import BookItem
from bs4 import BeautifulSoup

class BookContentSpider(RedisSpider):
    name = "bookContent"
    redis_key = "book_links"

    def parse(self, response):
        #todo
        pass
