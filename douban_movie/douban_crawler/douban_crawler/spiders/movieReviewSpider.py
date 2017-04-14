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
        content = '\n'.join(response.\
                xpath('//div[@property="v:description"]//text()').extract())
        if len(content) < 1500:
            return
        name = response.xpath('//header[@class="main-hd"]/a/text()').extract()[2]
        movie_link = response.xpath('//header[@class="main-hd"]/a/@href').extract()[1]
        title = response.xpath('//span[@property="v:summary"]/text()').extract()[0]
        author = response.xpath('//span[@property="v:reviewer"]/text()').extract()[0]
        author_link = response.xpath('//header[@class="main-hd"]/a/@href').extract()[0]
        content = content
        vote = response.xpath('//div[@class="main-panel-useful"]/button/text()').extract()
        up = int(''.join(re.findall('[0-9]*', vote[0])))
        down = int(''.join(re.findall('[0-9]*', vote[1])))
        rate = int(''.join(response.xpath('//span[@property="v:rating"]/text()').extract()[0]))
        
        item['url'] = response.url
        item['MovieName'] = name
        item['MovieLink'] = movie_link
        item['ReviewTitle'] = title
        item['ReviewAuthor'] = author
        item['AuthorLink'] = author_link
        item['ReviewContent'] = content
        item['UpNumber'] = up
        item['DownNumber'] = down
        item['Rate'] = rate

        yield item
