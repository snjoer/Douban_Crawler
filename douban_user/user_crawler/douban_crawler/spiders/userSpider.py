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
        
        host = self.settings['REDIS_HOST']
        item = UserItem()
        UN = response.xpath('//div[@class='info-section']/div[@class='name']').extract()[0]
        FN = response.xpath('//a[@href='/people/1887834/followed']/div[@class='count']').extract()[0]
        BN = response.xpath('//a[@href='/people/1887834/statuses']/div[@class='count']').extract()[0]
        DN = response.xpath('//a[@href='/people/1887834/doulists']/div[@class='count']').extract()[0]
        CN = response.xpath('//a[@href='/people/1887834/collection']/div[@class='count']').extract()[0]          
        item['UserName'] = UN
        item['FollowingNumber'] = FN
        item['BroadcastNumber'] = BN
        item['DoulistsNumber'] = DN
        item['CollectionNumbe'] = CN
        item['HomeUrl'] = response.url
        
        yield item
        pass

    def getFollowingUsers(self, response):
        # get links of following member
        # yield corresponding requests
        # use parse as callback function
        pass
