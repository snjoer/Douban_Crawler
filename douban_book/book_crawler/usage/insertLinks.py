#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import redis

r = redis.Redis(host='localhost', port=6379)

with open('review_links', 'r') as f:
    lines = f.readlines()
    for line in lines:
        r.lpush('review_links', line)
