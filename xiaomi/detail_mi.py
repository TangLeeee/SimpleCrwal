import requests
import json
from bs4 import BeautifulSoup
import time


BASE_URL = "http://app.mi.com/details?id=%s"
tarPackage = "com.baidu.xifan"




fin = open('xiaomi.csv')
lines = fin.readlines()
fin.close()

fout = open('xiaomi_detail.csv','a')


stPos = 1883

tot = 0
for line in lines:
    tl = line.strip().split(',')
    print tot
    tarPackage = tl[1]
    print tarPackage

    if tot < stPos:
        tot += 1
        continue

    res = requests.get(BASE_URL % tarPackage)
    soup = BeautifulSoup(res.text, "html.parser")

    introItem =  soup.select('.intro-titles')[0]
    companyName =  introItem.select('p')[0].string.encode('utf8')
    starNumber = introItem.select('.star1-empty div')[0]['class'][1][-1].encode('utf8')
    commentNumber = introItem.select('.app-intro-comment')[0].string[2:-5].encode('utf8')

    lookItem = soup.select('.look-detail ul')[0].select('li')
    softwareSize = lookItem[1].string.encode('utf8')
    versionNumber = lookItem[3].string.encode('utf8')
    updateTime = lookItem[5].string.encode('utf8')

    appText = soup.select('.app-text p')[0].get_text().encode('utf8')

    curInfo = "%s,%s,%s,%s,%s,%s,%s\n" % (line.strip(), companyName, starNumber, commentNumber, softwareSize, versionNumber, updateTime)

    fout.write(curInfo)
    
    finfo = open('info/%d.txt' % tot, 'w')
    finfo.write(curInfo)
    finfo.write(appText)
    finfo.close()
    tot += 1
    time.sleep(1)

fout.close()

