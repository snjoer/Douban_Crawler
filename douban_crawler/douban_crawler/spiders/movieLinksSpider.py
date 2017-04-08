'''

This spider crawls iterates index pages and then release movie links 
to Redis Database with redis_key: "movie_links"

'''    
import os
import scrapy

class DoubanMovieSpider(scrapy.Spider):
    count = 0
    total = 0
    name = "movieLinks"
    start_urls = ["https://movie.douban.com/tag/2016",]

    def parse(self, response):
        url = response.url
        lists = response.xpath('//div[@class="pl2"]/a/@href').extract()

        for li in lists:
            command = "redis-cli lpush movie_links " + li
            os.system(command)

        if self.count == 0:
            num = int(response.xpath('//span[@class="thispage"]/@data-total-page').extract()[0])
#            self.total = num * 20
            self.total = 20

        self.count += 20

        if self.count < self.total:
            new_url = self.start_urls[0] + '?start=' + str(self.count)
            yield scrapy.Request(new_url, callback=self.parse)
        else:
            self.count = 0
