#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import os
import sys

if __name__ == '__main__':
    start = int(sys.argv[2])
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
        i = 0
        end = 100 + start
        for line in lines:
            if i >= start:
                if i == end:
                    break
                os.system('redis-cli lpush more_reviews ' + line)  
            i += 1
