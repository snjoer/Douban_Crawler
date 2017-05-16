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
    with open('review_links', 'a') as f:
        while True:
            try:
                source, data = redis_conn.blpop(['review_links'],\
                        timeout=1)
            except:
                break
            f.write(data + '\n')

main()
