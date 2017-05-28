# -*- coding: utf-8 -*-

import random
import string
from fake_useragent import UserAgent
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware

class RotateUserAgentMiddleware(UserAgentMiddleware):
    def process_request(self,request, spider):
        user_agent = UserAgent()
        ua = user_agent.random
        if ua:
            #print ua
            print "********Current UserAgent:%s************" %ua  
            #log.msg('Current UserAgent: '+ua, level='INFO') 
            request.headers.setdefault('User-Agent', ua)
