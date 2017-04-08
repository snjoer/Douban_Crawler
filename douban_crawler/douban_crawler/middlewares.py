# -*- coding: utf-8 -*-

from fake_useragent import UserAgent
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware

class RotateUserAgentMiddleware(UserAgentMiddleware):
    def __init__(self,user_agent=''):
        self.user_agent = user_agent
        
    def process_request(self,request,spider):
        ua = UserAgent() 
        print "********Current UserAgent:%s************" %ua  
        #log.msg('Current UserAgent: '+ua, level='INFO') 
        request.headers.setdefault('User-Agent', ua.random)
            
class ProxyMiddleware(object):
    
    #从数据库中读取代理url
    proxyList = ['218.92.220.58:8080', '43.226.162.23:80', '27.148.151.27:80', '124.88.67.7:843']
    
    def process_request(self, request, spider):
        pass
        # Set the location of the proxy
        pro_adr = random.choice(self.proxyList)
        print "*******-----------*Current Proxy IP:%s*-----------***********" %pro_adr
        #request.meta['proxy'] = "http://{}:{}@{}:{}".format(user,pass,'127.0.0.1','8118')
        request.meta['proxy'] = "http://"+ pro_adr
