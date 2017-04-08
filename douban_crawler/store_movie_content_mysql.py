#!/usr/bin/env python
# -*- encoding:utf-8 -*-

'''
Database: Douban_Movies
Table: Douban_Movies

Table Structure:
CREATE TABLE Douban_Movies (
Name varchar(500) NOT NULL, 
PostUrl varchar(200) NOT NULL,
Director varchar(300) NOT NULL, 
Release_Time varchar(500) NOT NULL, 
Area varchar(500) NOT NULL,
Performers varchar(500) NOT NULL)CHARSET=utf8mb4;
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
                sql = 'INSERT INTO Douban_Movies VALUES \
                        ("%s", "%s", "%s", "%s");' %\
                        (item['MovieName'],\
                        item['PostUrl'],\
                        item['Director'],\
                        item['ReleaseTime'],\
                        item['Area'],\
                        item['Performers'])
                cursor.execute(sql)
                mysql_conn.commit()
                print "Insert one"
        except Exception, e:
            print e.message
            with open('failed_content', 'a') as f:
                f.write(item['url'] + '\n')

if __name__ == '__main__':
    main()
