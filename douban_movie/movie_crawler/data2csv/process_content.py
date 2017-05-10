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
    writer.writerow(['电影名','海报链接','导演','上映时间','地区','表演者'])
    while True:
        try:
            source, data = redis_conn.blpop(['content:items'],\
                    timeout=1)
        except:
            break
        item = json.loads(data)
        data = [item['MovieName'],\
                item['PostUrl'],\
                item['Director'],\
                item['ReleaseTime'],\
                item['Area'],\
                item['Performers']]
        writer.writerow(data)
    csvfile.close()

main()
