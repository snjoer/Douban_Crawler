'''

This spider gets start url using key "start_url".
It fetches user data and yield corresponding item.
Yield requests of his/her following Users to crawl recursively.

'''

import re
import scrapy
from scrapy_redis.spiders import RedisSpider
from douban_crawler.items import UserItem

class DoubanUserSpider(RedisSpider):
    name = "doubanUser"
    redis_key = "start_url"

    def parse(self, response):
        # parse proper link for getInfo and getFollwingUsers
        # call getInfo to get user info.
        # call getFollowingUsers to get following user link.
        # yield item and requests.
        pass
    
    def getInfo(self, response):
        # gets user info, yield item
        pass

    def getFollowingUsers(self, response):
        # gets following users link
        # callback parse method to crawl all following users continuously
        pass
