'''

This spider extracts review content from the given link of "review_links" 
which can be accessed from Redis Database by redis_key: "review_links" 
and stores the content to HBase Database.

'''

import scrapy
from scrapy_redis.spiders import RedisSpider
from douban_crawler.items import ReviewItem

class MovieReviewSpider(RedisSpider):
    name = "review"
    redis_key = "review_links"

    def parse(self, response):
        for sel in response.xpath('div[@id="link-report"]'):
            item = DoubanCrawlerItem_review
            item['ReviewContent'] = sel.xpath('p/text()').extract()
            yield items

        # todo
        pass
