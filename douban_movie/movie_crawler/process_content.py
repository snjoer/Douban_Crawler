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
    csvfile = file('csvfile.csv', 'a')
    while True:
        try:
            source, data = redis_conn.blpop(['movieContent:items'],\
                    timeout=1)
        except:
            break
        item = json.loads(data)
        writer = csv.writer(csvfile)
        data = [item['MovieName'],\
                item['PostUrl'],\
                item['Director'],\
                item['ReleaseTime'],\
                item['Area'],\
                item['Performers'],\
                item['Rate']]
        writer.writerow(data)
    csvfile.close()

main()
