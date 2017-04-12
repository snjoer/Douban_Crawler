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

    def open_spider(self, spider):
        logging.info('open hbase to host %s when spider:%s open' %
                     (HBASE_CFG['host'], spider.name))
        self.hbase.open()
        self.hbase.specify_table(HBASE_CFG['table_name'])

    def close_spider(self, spider):
        logging.info('close hbase to host %s when spider:%s open' %
                     (HBASE_CFG['host'], spider.name))
        self.hbase.close()

    def process_item(self, item, spider):
        if spider.name is not 'movieContent':
            return item
        
        process_item.process_movie_item(self.hbase, item['MovieName'], HBASE_CFG['family'], item)

        logging.debug('movie:%s has been handled'%item['MovieName'])

        return item
