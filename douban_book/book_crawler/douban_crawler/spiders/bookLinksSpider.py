'''
This spider crawls iterates index pages and then release movie links 
to Redis Database with redis_key: "book_links"
'''
import scrapy
import logging
from scrapy_redis.spiders import RedisSpider
import os

class BookLinksSpider(scrapy.Spider):

    start_urls = ["https://book.douban.com/subject/1000001/",]
    name = "bookeLinks"
    sbject = 10000001
    def parse(self, response):
 
        host = self.settings['REDIS_HOST']
        lists = "https://book.douban.com/subject/ + 'subject' + /",
             
        for li in lists:
            command = "redis-cli -h" + host + " lpush book_links " \
                    + li.extract()
            os.system(command)
      
        if subject < 7999999 && >= 1000001
            subject = subject + 1
            url = "https://book.douban.com/subject/ + 'subject' + /"
            yield scrapy.Request(url, callback=self.parse) 
        
        else
            if subject < 10000002 
                subject = 10000002
                url = "https://book.douban.com/subject/ + 'subject' + /"
                yield scrapy.Request(url, callback=self.parse) 
            if subject > 20496602
                logging.log(logging.INFO, '*** finished crawling ... ')
                return
            else
                subject = subject + 1
                 url = "https://book.douban.com/subject/ + 'subject' + /"
                yield scrapy.Request(url, callback=self.parse) 
