# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging
import time

from settings import hbase

class DoubanCrawlerPipeline(object):
    def process_item(self, item, spider):
        return item


class hbasepipeline(object):
    def __init__(self):
        self.conn = happybase.Connection(
                host = hbase['host'],
                table_prefix = hbase['namespace'],
                table_prefix_separator = ":")

        self.conn.open()
        self.table = self.conn.table(hbase['table_name'])
        self.batch = self.table.batch(batch_size = hbase['batch_size'])
        self.row = 0

    def process_item(self, item, spider):
	if spider.name is not 'movieContent':
	    return item

        try:
	    logging.msg("[+] " + item["MovieName"] )
            self.batch.put(item['MovieName'], {"Movie:PostUrl": item['PostUrl'], 'Movie:Director': item['Director'], "Movie:ReleaseTime": item['ReleaseTime'], "Movie:Area": item['Area'], "Movie:Performers": item['Performers']})
            self.batch.send()
        except:
	    logging.msg("[-] %s Failed." % item["MovieName"])
        finally:
            self.conn.close()

        return item
