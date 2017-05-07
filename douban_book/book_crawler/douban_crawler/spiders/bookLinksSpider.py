# -*- encoding:utf-8 -*-   
'''
This spider crawls iterates index pages and then release movie links 
to Redis Database with redis_key: "book_links"
'''
import scrapy
import logging
from scrapy_redis.spiders import RedisSpider
import sys
import os

reload(sys)
sys.setdefaultencoding('utf-8')

class BookLinksSpider(scrapy.Spider):

    start_urls = ["https://book.douban.com/subject/1000001/",]
    name = "bookLinks"
    subject = 10000001
    def parse(self, response):
 
        host = self.settings['REDIS_HOST']
        logo = ''.join(response.xpath("//div[@class='nav-logo']/a/text()").extract_first().split())
             
        if logo == '豆瓣读书':
            command = "redis-cli -h " + host + " lpush book_links " \
                    + response.url
            os.system(command)
      
        self.subject += 1
        if self.subject < 7999999 and self.subject >= 1000001:
            url = "https://book.douban.com/subject/" + str(self.subject) + "/"
            yield scrapy.Request(url, callback=self.parse) 
        
        else:
            if self.subject < 10000002: 
                self.subject = 10000002
                url = "https://book.douban.com/subject/" + str(self.subject) + "/"
                yield scrapy.Request(url, callback=self.parse) 
            if self.subject > 20496602:
                logging.log(logging.INFO, '*** finished crawling ... ')
                return
            else:
                url = "https://book.douban.com/subject/" + str(self.subject) + "/"
                yield scrapy.Request(url, callback=self.parse) 
