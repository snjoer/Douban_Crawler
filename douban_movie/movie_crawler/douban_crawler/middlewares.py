# -*- coding: utf-8 -*-

import random
import string
import telnetlib
import json
from scrapy.conf import settings
from fake_useragent import UserAgent
from ProxyYourSpider import pys
from scrapy.downloadermiddlewares.retry import RetryMiddleware
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

class ProxyMiddleware(object):
    def process_request(self, request, spider):
        https_proxy = settings.get('HTTPS_PROXY')
        print "*******-----------*Current Proxy IP:%s*-----------***********" % https_proxy
        request.meta['proxy'] = https_proxy

class CustomRetryMiddleware(RetryMiddleware):
    def process_response(self, request, response, spider):
        if response.status != 200:
            return self._retry(request) or response
        return response
