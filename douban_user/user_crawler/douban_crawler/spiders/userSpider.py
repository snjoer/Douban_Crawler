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
        item = UserItem()
        item['UserName'] = ''.join(response.\
                xpath('//div[@class="name"]/text()').\
                extract_first().split())
        href = response.xpath('//div[@class="profile-nav"]/a/@href').\
                extract_first()
        uid = ''.join(re.findall('[0-9]*',href))
        dataUrl = 'https://m.douban.com/rexxar/api/v2/user/' + uid
        followedUrl = 'https://m.douban.com/rexxar/api/v2/user/' \
                + uid + '/following?start=0'
        yield scrapy.Request(url=dataUrl, meta={'item':item}, \
                callback=self.getInfo)
        yield scrapy.Request(url=followedUrl, \
                callback=self.getFollowingUsers)

    def getInfo(self, response):
        item = response.meta['item']
        data = json.loads(response.text)
        collection = data['collected_subjects_count']
        url = data['url']
        following_count = data['following_count']
        broadcast = data['statuses_count']
        doulists = data['owned_doulist_count']
        item['FollowingNumber'] = following_count
        item['BroadcastNumber'] = broadcast
        item['DoulistsNumber'] = doulists
        item['CollectionNumber'] = collection
        item['HomeUrl'] = url
        yield item

    def getFollowingUsers(self, response):
        url = response.url
        urls = url.split('=')
        count = int(urls[-1])
        count += 20
        data = json.loads(response.text)
        users = data['users']
        if users != []:
            for user in users:
                userLink = user['url'].replace('www', 'm')
                yield scrapy.Request(url=userLink,callback=self.parse)
            url = urls[0] + '=' + str(count)
            yield scrapy.Request(url=url, callback=self.getFollowingUsers)
