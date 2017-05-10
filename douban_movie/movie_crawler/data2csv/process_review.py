#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import sys
import csv
import json
import redis

reload(sys)
sys.setdefaultencoding('utf-8')

def connectRedis():
    conn = redis.StrictRedis(host='localhost', port=6379, password='kNlTR2nPrv')
    return conn

def main():
    redis_conn = connectRedis()
    csvfile = file('csvfile.csv', 'a')
    writer = csv.writer(csvfile)
    writer.writerow(['电影名','电影链接','评论标题','评论作者','作者主页','评论内容','有用数','没用数', '作者评分'])
    while True:
        try:
            source, data = redis_conn.blpop(['review:items'],\
                    timeout=1)
        except:
            break
        item = json.loads(data)
        data = [item['MovieName'],\
                item['MovieLink'],\
                item['ReviewTitle'],\
                item['ReviewAuthor'],\
                item['AuthorLink'],\
                item['ReviewContent'],\
                item['UpNumber'],\
                item['DownNumber'],\
                item['Rate']]
        writer.writerow(data)
    csvfile.close()

main()
