import scrapy
from scrapy.redis.spider import RedisSpider

class DoubanMovieSpider(RedisSpider):
    name = "doubanMovie"

    def parse(self, response):
        # todo
        pass
