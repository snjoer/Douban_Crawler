# -*- coding: utf-8 -*-

import random
import telnetlib
import json
import scrapy
import sys
from scrapy import log
from settings import FAILED_CODES
from fake_useragent import UserAgent
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware

class RotateUserAgentMiddleware(UserAgentMiddleware):
        
    def process_request(self,request,spider):
        user_agent = UserAgent()
        ua = user_agent.random
        if ua:
            log.msg('Current UserAgent: '+ua, level=log.INFO) 
            request.headers.setdefault('User-Agent', ua)

class saveFailedMiddleware():
    
    def process_response(self, request, response, spider):
        if response.status in FAILED_CODES:
            with open('failed_request', 'a') as f:
                f.write(response.url + '\n')
        return response

'''
class ProxyMiddleware(object):
    #读取代理url
    #文件路径可能要根据自己机子的环境改一下
    # proxyList = ["218.92.220.58:8080", "43.226.162.23:80", "27.148.151.27:80", "124.88.67.7:843"]

    dbTools = sqlTools()
    proxyList = dbTools.getIpPool()
    #测试ip是否可用
    #return 'xxx.xxx.xxx.xxx:port'
    def getPropertyIp(self,l):
        def testIp(ip,port):
            print 'testing '+ip+':'+port+'...'
            try:
                telnetlib.Telnet(ip,port=port,timeout=20)
            except:
                print ip+':'+port+' can not be used!!!'
                return False
            else:
                print ip+':'+port+' success!!!'
                return True
        ipSucc = False
        while not ipSucc:
            pro_adr = str.split(random.choice(l),':')
            ipSucc = testIp(pro_adr[0],pro_adr[1])
        return ':'.join(pro_adr)
    
    def process_request(self, request, spider):
        pro_adr = self.getPropertyIp(self.proxyList)
        print "*******-----------*Current Proxy IP:%s*-----------***********" %pro_adr
        #request.meta['proxy'] = "http://{}:{}@{}:{}".format(user,pass,'127.0.0.1','8118')
        request.meta['proxy'] = "http://"+ pro_adr
'''
