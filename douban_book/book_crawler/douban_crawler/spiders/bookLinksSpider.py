'''
This spider crawls iterates index pages and then release movie links 
to Redis Database with redis_key: "book_links"
'''
import scrapy
import os

class BookLinksSpider(scrapy.Spider):

    start_urls = ["https://book.douban.com/subject/1000001/",]
    name = "bookeLinks"

    def parse(self, response):
        #todo
        pass
