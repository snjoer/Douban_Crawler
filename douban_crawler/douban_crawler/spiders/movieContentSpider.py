'''

This spider extracts specific content from given movie links which can be 
accessed from Redis Data base by key word "movie_links" and stores the data
to HBase.
Moreover, this spider should export link to more reviews to Redis Database
as key word "more_reviews".

'''

import scrapy
from scrapy.redis.spider import RedisSpider

class MovieContentSpider(RedisSpider):
    name = "movieContent"
    redis_key = "movie_links"

    def parse(self, response):
        # todo
        pass
