#!/usr/bin/env python
# -*- encoding:utf-8 -*-

'''
Database: Douban_Movies
Table: Reviews

Table Structure:
CREATE TABLE Reviews 
(Name varchar(100) NOT NULL, 
Title varchar(200) NOT NULL, 
Author varchar(50) NOT NULL, 
Content varchar(3000) NOT NULL, 
UpNumber INT NOT NULL, 
DownNumber INT NOT NULL,
Rate INT NOT NULL)CHARSET=utf8;
'''

import json
import redis
import pymysql.cursors

def connectRedis():
    conn = redis.StrictRedis(host='localhost', port=6379)
    return conn

def connectMySQL():
    conn = pymysql.connect(host='localhost',
                             user='root',
                             db='douban_movies',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)
    return conn

def main():
    redis_conn = connectRedis()
    mysql_conn = connectMySQL()
    while True:
        source, data = redis_conn.blpop(['review:items'])
        item = json.loads(data)
        try:
            with mysql_conn.cursor() as cursor:
                sql = "INSERT INTO Reviews VALUES \
                        ('%s', '%s', '%s', '%s', %d, %d, %d);" %\
                        (item['MovieName'], item['ReviewTitle'],\
                        item['ReviewAuthor'], item['ReviewContent'],\
                        item['UpNumber'], item['DownNumber'], item['Rate'])
                cursor.execute(sql)
                mysql_conn.commit()
        except Exception as e:
            print e.message

if __name__ == '__main__':
    main()
