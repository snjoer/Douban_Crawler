# -*- coding: UTF-8 -*- 
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
        item = ReviewItem()
        try:
            name = response.xpath('//header[@class="main-hd"]/a/text()').extract()[2]
        except:
            name = ''
        try:
            book_link = response.xpath('//header[@class="main-hd"]/a/@href').extract()[1]
        except:
            book_links = ''
        try:
            title = response.xpath('//span[@property="v:summary"]/text()').extract()[0]
        except:
            title = ''
        try:
            author = response.xpath('//span[@property="v:reviewer"]/text()').extract()[0]
        except:
            author = ''
        try:
            author_link = response.xpath('//header[@class="main-hd"]/a/@href').extract()[0]
        except:
            author_link = ''
        try:
            content = '\n'.join(response.\
                xpath('//div[@property="v:description"]//text()').extract())
        except:
            content = ''
        if len(content) < 1500:
            return
        try:
            vote = response.xpath('//div[@class="main-panel-useful"]/button/text()').extract()
        except:
            vote = ''
        try:
            up = int(''.join(re.findall('[0-9]*', vote[0])))
        except:
            up = ''
        try:
            down = int(''.join(re.findall('[0-9]*', vote[1])))
        except:
            down = ''
        try:
            rate = response.xpath('//span[@property="v:rating"]/text()').extract()[0]
        except:
            rate = 0

        item['BookName'] = name
        item['BookLink'] = book_link
        item['ReviewTitle'] = title
        item['ReviewAuthor'] = author
        item['AuthorLink'] = author_link
        item['ReviewContent'] = content
        item['UpNumber'] = up
        item['DownNumber'] = down
        item['Rate'] = rate

        yield item
