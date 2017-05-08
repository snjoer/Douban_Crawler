# -*- encoding:utf-8 -*-
'''

This spider extracts specific content from given book links which can be 
accessed from Redis Database by redis_key "book_links" and stores the data
to HBase.
Moreover, this spider should export link to more reviews to Redis Database
as redis_key "more_reviews".

'''
import re,os
from scrapy_redis.spiders import RedisSpider
from douban_crawler.items import BookItem

class BookContentSpider(RedisSpider):
    name = "bookContent"
    redis_key = "book_links"

    def parse(self, response):

        item = BookItem()

        bookname = response.xpath('//*[@id="wrapper"]/h1/span/text()').extract()[0]
        try:
            posturl = response.xpath('//*[@id="mainpic"]/a/img').re(u'src="(.*)" title="点击看大图"')[0]
        except:
            posturl = ''
        try:
            author = response.xpath('//*[@id="info"]/a[1]/text()').extract()[0]
        except:
            author = ''
        new_author = re.sub(re.compile('\s+'), '', author)
        try:
            releasetime = response.xpath('//*[@id="info"]').re(u'<span class="pl">出版年:</span>(.*)<br>')[0]
        except:
            releasetime = ''
        new_releasetime = re.sub(re.compile('\s+'), '', releasetime)
        try:
            press = response.xpath('//*[@id="info"]').re(u'<span class="pl">出版社:</span>(.*)<br>')[0]
        except:
            press = ''
        new_press = re.sub(re.compile('\s+'), '', press)
        try:
            rate = response.xpath('//div[@typeof="v:Rating"]//text()').extract()[1]
        except:
            rate = ''
        item['BookName'] = bookname
        item['PostUrl'] = posturl
        item['Author'] = new_author
        item['ReleaseTime'] = new_releasetime
        item['Press'] = new_press
        item['Rate'] = rate

        #comment_url
        comment_url = re.sub(re.compile('\?icn=index-topchart-subject'),'reviews',response.url)
        host = self.settings['REDIS_HOST']
        command = 'redis-cli -h ' + host + ' lpush more_reviews ' + comment_url
        os.system(command)
        yield item
