#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import os
import sys
import redis


begin = int(sys.argv[2])
end = int(sys.argv[3])

i = 0

with open(sys.argv[1], 'rb') as f:
    lines = f.readlines()
    for line in lines:
        if i >= begin:
            line = ''.join(line.split()) + '/'
            command = "redis-cli lpush book_links " + line
            os.system(command)
        i += 1
        if i >= end:
            break
