#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import os
import sys

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
        for line in lines:
            os.system('redis-cli -a kNlTR2nPrv lpush more_reviews ' + line + '/')  
