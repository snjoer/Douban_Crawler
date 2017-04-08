# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    url = scrapy.Field()
    MovieName = scrapy.Field()
    Director = scrapy.Field()
    ReleaseTime = scrapy.Field()
    Country = scrapy.Field()


class ReviewItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    url = scrapy.Field()
    MovieName = scrapy.Field()
    ReviewTitle = scrapy.Field()
    ReviewAuthor = scrapy.Field()
    ReviewContent = scrapy.Field()
    UpNumber = scrapy.Field()
    DownNumber = scrapy.Field()
    Rate = scrapy.Field()
