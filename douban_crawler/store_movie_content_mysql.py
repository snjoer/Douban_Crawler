#!/usr/bin/env python
# -*- encoding:utf-8 -*-

'''
Database: Douban_Movies
Table: Douban_Movies

Table Structure:
CREATE TABLE Douban_Movies (
Name varchar(200) NOT NULL, 
Director varchar(100) NOT NULL, 
Release_Time varchar(50) NOT NULL, 
Country varchar(50) NOT NULL)CHARSET=utf8mb4;
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
        source, data = redis_conn.blpop(['movieContent:items'])
        item = json.loads(data)
        try:
            with mysql_conn.cursor() as cursor:
                sql = "INSERT INTO Douban_Movies VALUES \
                        ('%s', '%s', '%s', '%s');" %\
                        (item['MovieName'],\
                        item['Director'],\
                        item['ReleaseTime'],\
                        item['Country'])
                cursor.execute(sql)
                mysql_conn.commit()
        except Exception as e:
            print e.message

if __name__ == '__main__':
    main()
