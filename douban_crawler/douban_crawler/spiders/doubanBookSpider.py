import scrapy
from scrapy_redis.spiders import RedisSpider

class DoubanBookSpider(RedisSpider):
    name = "doubanBook"

    def parse(self, response):
        # todo
        pass
