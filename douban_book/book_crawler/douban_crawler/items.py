# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BookItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    BookName = scrapy.Field()
    PostUrl = scrapy.Field()
    Author = scrapy.Field()
    ReleaseTime = scrapy.Field()
    Press = scrapy.Field()
    Rate = scrapy.Field()

class ReviewItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    BookName = scrapy.Field()
    BookLink = scrapy.Field()
    ReviewTitle = scrapy.Field()
    ReviewAuthor = scrapy.Field()
    AuthorLink = scrapy.Field()
    ReviewContent = scrapy.Field()
    UpNumber = scrapy.Field()
    DownNumber = scrapy.Field()
    Rate = scrapy.Field()
