'''

This spider extracts review content from the given link of "review_links" 
which can be accessed from Redis Database by redis_key: "review_links" 
and stores the content to HBase Database.

'''

import re
import scrapy
from scrapy_redis.spiders import RedisSpider
from douban_crawler.items import ReviewItem

class MovieReviewSpider(RedisSpider):
    name = "review"
    redis_key = "review_links"

    def parse(self, response):
        item = ReviewItem()
        name = response.xpath('//header[@class="main-hd"]/a/text()').extract()[2]
        title = response.xpath('//span[@property="v:summary"]/text()').extract()[0]
        author = response.xpath('//span[@property="v:reviewer"]/text()').extract()[0]
        content = '\n'.join(response.\
                xpath('//div[@property="v:description"]/p//text()').extract())
        vote = response.xpath('//div[@class="main-panel-useful"]/button/text()').extract()
        up = int(''.join(re.findall('[0-9]*', vote[0])))
        down = int(''.join(re.findall('[0-9]*', vote[1])))
        rate = int(''.join(response.xpath('//span[@property="v:rating"]/text()').extract()[0]))

        item['MovieName'] = name
        item['ReviewTitle'] = title
        item['ReviewAuthor'] = author
        item['ReviewContent'] = content
        item['UpNumber'] = up
        item['DownNumber'] = down
        item['Rate'] = rate

        yield item
