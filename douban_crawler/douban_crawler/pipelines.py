# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import logging
import process_item
from hbase_instance import HbaseInstance
from settings import HBASE_CFG


class DoubanCrawlerPipeline(object):

    def process_item(self, item, spider):
        return item


class HbasePipeline(object):

    def __init__(self):
        self.hbase = HbaseInstance(HBASE_CFG)
        self.hbase_is_open = False
        self.content_spider_name = 'movieContent'
        self.review_spider_name = 'review'
        self.content_spider_is_closed = False
        self.review_spider_is_closed = False

    def is_right_spider(self, spider):
        return spider.name == self.content_spider_name or spider.name == self.review_spider_name

    def open_spider(self, spider):
        if self.hbase_is_open:
            return

        if not self.is_right_spider(spider):
            return

        logging.info('open hbase to host %s when spider:%s open' %
                     (HBASE_CFG['host'], spider.name))
        self.hbase.open()
        self.hbase.specify_table(HBASE_CFG['table_name'])
        self.hbase_is_open = True

    def close_spider(self, spider):
        if self.name == self.content_spider_name:
            self.content_spider_is_closed = True
        elif self.name == self.review_spider_name:
            self.review_spider_is_closed = True

        if self.content_spider_is_closed and self.review_spider_is_closed:
            logging.info('close hbase to host %s when spider:%s close' %
                         (HBASE_CFG['host'], spider.name))
            self.hbase.close()
            self.hbase_is_open = False

    def process_item(self, item, spider):
        if spider.name is self.content_spider_name:
            process_item.process_movie_item(
                self.hbase, item['MovieName'], HBASE_CFG['movie_family'], item)
            logging.debug('movie:%s content has been handled' %
                          item['MovieName'])

        elif spider.name is self.review_spider_name:
            process_item.process_review_item(
                self.hbase, item['MovieName'], HBASE_CFG['review_family'], item)
            logging.debug('movie:%s review has been handled' %
                          item['MovieName'])

        return item
