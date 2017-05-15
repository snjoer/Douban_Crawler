# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class UserItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    UserName = scrapy.Field()
    FollowingNumber = scrapy.Field()
    BroadcastNumber = scrapy.Field()
    DoulistsNumber = scrapy.Field()
    CollectionNumber = scrapy.Field()
    HomeUrl = scrapy.Field()

