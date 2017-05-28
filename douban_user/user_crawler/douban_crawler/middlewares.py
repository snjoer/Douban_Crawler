# -*- coding: utf-8 -*-

import random
import telnetlib
import json
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware

class RotateUserAgentMiddleware(UserAgentMiddleware):
    def __init__(self,user_agent=''):
        self.user_agent = user_agent
        
    def process_request(self,request,spider):
        ua = random.choice(self.user_agent_list)
        if ua:
            #print ua
            print "********Current UserAgent:%s************" %ua  
            #log.msg('Current UserAgent: '+ua, level='INFO') 
            request.headers.setdefault('User-Agent', ua)
            
    user_agent_list = [ \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1" \
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11", \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6", \
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6", \
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1", \
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5", \
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5", \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3", \
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24", \
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    ]

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
