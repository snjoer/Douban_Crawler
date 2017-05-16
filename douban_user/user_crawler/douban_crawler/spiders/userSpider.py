'''
This spider gets start url using key "start_url".
It fetches user data and yield corresponding item.
Yield requests of his/her following Users

'''

import re
import json
import scrapy
from scrapy_redis.spiders import RedisSpider
from douban_crawler.items import UserItem

class DoubanUserSpider(RedisSpider):
    name = "doubanUser"
    redis_key = "start_url"

    def parse(self, response):
        # get uid
        # construct userinfo link and following link
        # yield corresponding requests
        pass

    def getInfo(self, response):
        # get user info
        # yield items
        pass

    def getFollowingUsers(self, response):
        # get links of following member
        # yield corresponding requests
        # use parse as callback function
        pass
