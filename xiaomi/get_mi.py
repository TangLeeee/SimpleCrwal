import requests
import json
from bs4 import BeautifulSoup
import time

BASE_URL = "http://app.mi.com/categotyAllListApi?page=%d&categoryId=2&pageSize=200"
res = requests.get(BASE_URL)
curItem =  res.json()
print len(curItem['data'])


fin = open('xiaomi.csv','w')

for i in range(10):
    res = requests.get(BASE_URL % i)
    curList =  res.json()
    for item in curList['data']:
        curName = item['displayName'].replace(',' ,' ').encode('utf8')
        curPackage = item['packageName'].encode('utf8')
        curId = item['appId']
        print curName
        fin.write('%s,%s,%d\n' % (curName, curPackage, curId))

fin.close()
