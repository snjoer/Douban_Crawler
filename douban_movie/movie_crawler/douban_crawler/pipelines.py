# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import logging
import process_item
import sqlite3


class DoubanCrawlerPipeline(object):
    pass

class SQLiteStorePipeline(object):
    def __init__(self):
        # settings = get_project_settings()
        # self.__class__.sqlite_name = settings.get('sqlite_name')
        # self.conn = sqlite3.connect(str(self.__class__.sqlite_name))
        self.conn = sqlite3.connect('sample.db')
    def process_item(self, item, spider):
        try:
            cursor = self.conn.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS broad 
                    (MovieName TEXT NOT NULL, 
                    MovieLink TEXT NOT NULL, 
                    ReviewTitle TEXT NOT NULL,
                    ReviewAuthor TEXT NOT NULL,
                    AuthorLink TEXT NOT NULL,
                    ReviewContent TEXT NOT NULL,
                    UpNumber TEXT NOT NULL,
                    DownNumber TEXT NOT NULL,
                    Rate TEXT NOT NULL)""")
            record = (item['MovieName'], \
                    item['MovieLink'], \
                    item['ReviewTitle'], \
                    item['ReviewAuthor'], \
                    item['AuthorLink'], \
                    item['ReviewContent'], \
                    item['UpNumber'], \
                    item['DownNumber'], \
                    item['Rate'])

            cursor.execute('INSERT INTO broad VALUES (?,?,?,?,?,?,?,?,?)', record)
            self.conn.commit()
        except sqlite3.ProgrammingError as e:
            print 'SQLite ERROR: ' + e.message

    def __del__(self):
        self.conn.close()
