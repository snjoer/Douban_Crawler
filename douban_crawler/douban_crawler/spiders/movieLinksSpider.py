'''

This spider crawls iterates index pages and then release movie links 
to Redis Database with redis_key: "movie_links"

'''

import scrapy
from scrapy.redis.spider import RedisSpider

class DoubanMovieSpider(RedisSpider):
    name = "movieLinks"

    def parse(self, response):
        # todo
        pass
