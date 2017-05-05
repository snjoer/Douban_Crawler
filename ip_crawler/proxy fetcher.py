import requests
from bs4 import BeautifulSoup
import json,telnetlib
import MySQLdb

class sqlTools():
    user = 'root'
    db = 'seedouban'
    pw = 'fsadqzwx199674'
    host = 'localhost'    
    def testIp(self,ip,port):
        print 'testing '+ip+':'+port+'...'
        try:
            telnetlib.Telnet(ip,port=port,timeout=20)
        except:
            print ip+':'+port+' can not be used!!!'
            return False
        else:
            print ip+':'+port+' success!!!'
            return True
    def getIpPool(self):
        ans = []
        db = MySQLdb.connect(user=self.user, db=self.db, passwd=self.pw, host=self.host)
        cursor = db.cursor()
        cursor.execute('select * from seedouban_ippool;')
        db.close()
        for data in cursor.fetchall():
            ans.append(data[1]+':'+data[2])
        return ans
    def setIpPool(self,index,ip,port):
        try:
            if self.testIp(ip,port):
                db = MySQLdb.connect(user=self.user, db=self.db, passwd=self.pw, host=self.host)
                cursor = db.cursor()
                print [index,ip,port]
                cursor.execute('insert into seedouban_ippool values(%s,%s,%s);',[index,ip,port])
                db.commit()
                db.close()
                return True
        except:
            return False
    def clearDb(self):
        db = MySQLdb.connect(user=self.user, db=self.db, passwd=self.pw, host=self.host)
        cursor = db.cursor()
        cursor.execute('delete from seedouban_ippool;')
        db.commit()
        db.close()
HEADERS = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}
url='http://www.xicidaili.com/'
res = requests.get(url,headers = HEADERS)
res.encoding = 'utf-8'
html = res.text
soup = BeautifulSoup(html,'html.parser')
td = soup.select('td')
# print(td[1].text)
group , temp = list(),list()
count , n = 1 , len(td)
while count < n:
    temp.append(td[count-1].text)
    if count % 8 ==0 :
        group.append(temp)
        temp = []
        if len(group) > 2:
            if group[-1][1] == group[-2][1]:
                # print(group[-1],group[-2],group[-3])
                group.pop()
                # print(group[-1], group[-2],group[-3])
    count = count + 1


L = []
dbFunc = sqlTools()
dbFunc.clearDb()
for each in group:
    ip = each[1]
    port = each[2]
    result = ip + ":" + port
    L.append(result)

for i,d in enumerate(L):
    index = i+1
    [ip,port] = str.split(d.encode('utf-8'),':')
    print index,ip,port
    dbFunc.setIpPool(index,ip,port)
