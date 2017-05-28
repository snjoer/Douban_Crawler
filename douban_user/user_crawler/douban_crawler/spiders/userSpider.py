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
        href = response.xpath('//link[@rel="canonical"]/@href').extract_first()
        uid = re.findall(r'[0-9]*',href)
        # construct userinfo link and following link
        url1 = 'https://m.douban.com/rexxar/api/v2/user/' + uid

        url2 = 'https://m.douban.com/rexxar/api/v2/user/' + uid + '/following?start=' + str(self.count)
        # yield corresponding requests
        yield scrapy.Request(url1, callback=self.getInfo)
        yield scrapy.Request(url2, callback=self.getFollowing) 

        pass

    def getInfo(self, response):
        
        host = self.settings['REDIS_HOST']
        item = UserItem()
        UN = response.xpath('//div[@class="info-section"]/div[@class="name"]').extract()[0]
        FN = response.xpath('//a[@href="/people/1887834/followed"]/div[@class="count"]').extract()[0]
        BN = response.xpath('//a[@href="/people/1887834/statuses"]/div[@class="count"]').extract()[0]
        DN = response.xpath('//a[@href="/people/1887834/doulists"]/div[@class="count"]').extract()[0]
        CN = response.xpath('//a[@href="/people/1887834/collection"]/div[@class="count"]').extract()[0]          
        item['UserName'] = UN
        item['FollowingNumber'] = FN
        item['BroadcastNumber'] = BN
        item['DoulistsNumber'] = DN
        item['CollectionNumbe'] = CN
        item['HomeUrl'] = response.url
        
        yield item
        pass

    def getFollowingUsers(self, response):
        dict = json.loads(response)
        for i in range(0, 20):
            id = dict['users'][i]['id']
            url = 'https://m.douban.com/rexxar/api/v2/user/' + id
            yield scrapy.Request(url, callback=self.parse)
        pass
