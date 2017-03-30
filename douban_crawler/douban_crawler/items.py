# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanCrawlerItem_movie(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    Movie Name = scrapy.Field()
    Director = scrapy.Field()
    Release Time= scrapy.Field()
    Country = scrapy.Field()


class DoubanCrawlerItem_review(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    Movie Name = scrapy.Field()
    Review Title = scrapy.Field()
    Review Author = scrapy.Field()
    Review Content = scrapy.Field()
    Up Number = scrapy.Field()
    Down Number = scrapy.Field()



pass
