# -*- coding: UTF-8 -*-
'''

This spider extracts specific content from given movie links which can be 
accessed from Redis Database by redis_key "movie_links" and stores the data
to HBase.
Moreover, this spider should export link to more reviews to Redis Database
as redis_key "more_reviews".

'''

import os
import sys
import scrapy
from scrapy_redis.spiders import RedisSpider
from douban_crawler.items import MovieItem

reload(sys)
sys.setdefaultencoding('utf-8')

class MovieContentSpider(RedisSpider):
    name = "movieContent"
    redis_key = "movie_links"

    def parse(self, response):
        host = self.settings['REDIS_HOST']
        item = MovieItem()
        name = response.xpath('//h1/span/text()').extract()[0].replace('"', '\'\'')
        director = response.xpath('//a[@rel="v:directedBy"]/text()').extract()[0].replace('"', '\'\'')
        time = response.xpath('//span[@property="v:initialReleaseDate"]/text()').extract()
        pls = response.xpath('//span[@class="pl"]')
        for pl in pls:
            text_list = pl.xpath('./text()').extract()
            if len(text_list) > 0:
                if text_list[0] == '制片国家/地区:':
                    country = pl.xpath('./following::text()').extract()[0]
        item['url'] = response.url
        item['MovieName'] = name
        item['Director'] = director
        item['ReleaseTime'] = ','.join(time)
        item['Country'] = country
        more_reviews = response.url + 'reviews'
        command = 'redis-cli -h ' + host + ' lpush more_reviews ' \
                + more_reviews
        os.system(command)
        yield item
