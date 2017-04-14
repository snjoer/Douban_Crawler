'''

This spider extracts specific content from given movie links which can be 
accessed from Redis Database by redis_key "movie_links" and stores the data
to HBase.
Moreover, this spider should export link to more reviews to Redis Database
as redis_key "more_reviews".

'''
import re,os
from scrapy_redis.spiders import RedisSpider
from douban_crawler.items import MovieItem
from bs4 import BeautifulSoup

class MovieContentSpider(RedisSpider):
    name = "movieContent"
    redis_key = "movie_links"

    def parse(self, response):
        data = response.body
        soup = BeautifulSoup(data,'"html.parser"')
        item = MovieItem()
        #MovieName
        for i in soup.find_all('h1'):
            p_1 = re.compile('\s+')
            p_2 = re.compile('\'')
            new_string = re.sub(p_1, '', i.text)
            new_string = re.sub(p_2, '|', new_string)
            MovieName = new_string
        #Director
        for i in soup.find_all('a', rel='v:directedBy'):
            Director = i.text
        #ReleaseTime
        for i in soup.find_all('span', property='v:initialReleaseDate'):
            ReleaseTime = i.text
        #Country
        info = soup.find('div', {'id': 'info'})
        span = info.find_all('span', {'class': 'pl'})[4]
        p_1 = re.compile('\s+')
        Country = re.sub(p_1, '', span.nextSibling)

        item['MovieName'] = MovieName
        item['Director'] = Director
        item['ReleaseTime'] = ReleaseTime
        item['Country'] = Country
        yield item

        #comment_url
        comment_url = soup.find_all('div', class_='mod-hd')[0].find_all('a', class_=None)[0]['href']
        command = "redis-cli lpush more_reviews " + comment_url
        os.system(command)
