#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import sys
import csv
import json
import redis

reload(sys)
sys.setdefaultencoding('utf-8')

def connectRedis():
    conn = redis.StrictRedis(host='localhost', port=6379)
    return conn

def main():
    redis_conn = connectRedis()
    csvfile = file('content.csv', 'a')
    writer = csv.writer(csvfile)
    while True:
        try:
            source, data = redis_conn.blpop(['bookContent:items'],\
                    timeout=1)
        except:
            break
        item = json.loads(data)
        data = [item['BookName'],\
                item['PostUrl'],\
                item['Author'],\
                item['ReleaseTime'],\
                item['Press'],\
                item['Rate']]
        writer.writerow(data)
    csvfile.close()

main()
