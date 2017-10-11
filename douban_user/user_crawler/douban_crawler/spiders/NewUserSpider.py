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
    name = "user"
    redis_key = "start_url"

    def parse(self, response):
        if response.status != 404:
            item = UserItem()
            item['UserName'] = ''.join(response.\
                    xpath('//div[@class="name"]/text()').\
                    extract_first().split())
            href = response.xpath('//div[@class="profile-nav"]/a/@href').\
                    extract_first()
            uid = ''.join(re.findall('[0-9]*',href))
            dataUrl = 'https://m.douban.com/rexxar/api/v2/user/' + uid
#            yield scrapy.Request(url=dataUrl, meta={'item':item}, \
#                    callback=self.getInfo) 
        next_user_id = int(response.url.split('/')[-2]) + 1
        next_url = response.url[0:-8] + str(next_user_id) + '/'
        print "offset: " + str(next_user_id)
        yield scrapy.Request(url=next_url, callback=self.parse)

    def getInfo(self, response):
        item = response.meta['item']
        data = json.loads(response.text)
        collection = data['collected_subjects_count']
        url = data['url']
        following_count = data['followers_count']
        broadcast = data['statuses_count']
        doulists = data['owned_doulist_count']
        item['FollowersNumber'] = following_count
        item['BroadcastNumber'] = broadcast
        item['DoulistsNumber'] = doulists
        item['CollectionNumber'] = collection
        item['HomeUrl'] = url
        yield item
