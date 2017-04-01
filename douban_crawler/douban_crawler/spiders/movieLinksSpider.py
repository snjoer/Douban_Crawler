'''

This spider crawls iterates index pages and then release movie links 
to Redis Database with redis_key: "movie_links"

'''    
import scrapy
from scrapy_redis.spiders import RedisSpider
import os

class DoubanMovieSpider(RedisSpider):
    count = 0
    total = 0


    url = "https://movie.douban.com/top250?start=0&filter="
    name = "movieLinks"
    redis_key = "movietop250"

def parse(self, response):


    url = response.url
    lists = response.xpath('.//div[@class="hd"]/a/@href').extract()[0]

    for li in lists:
        command = "redis-cli lpush movie_links " + li.extract()
        os.system(command)

    if self.count == 0:
        num = 10
        self.url = response.url
        self.total = num * 25

    self.count += 25

    if self.count < self.total:
        new_url = self.url + '?start=' + str(self.count)
        yield scrapy.Request(new_url, callback=self.parse)
    else:
        self.count = 0

        pass
