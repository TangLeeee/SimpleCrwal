import requests
from bs4 import BeautifulSoup
import time
import re

detailRe = re.compile('<p class="art-content">(.*?)</p>')

BASE_URL = "http://www.appchina.com"

f = open('appchina.csv')

lines = f.readlines()

f.close()

CMD = '%d,%s,%s,%s,%s,%s,%s,"%s"\n'

fout = open('appChina_detail.csv','a')

for i in range(len(lines)):
    print i
    line = lines[i]
    tL = line.split(',')
    appName = tL[0]
    appUrl = tL[1]
    appIntro = line[len(tL[0]) + len(tL[1]) + 3:-2]
    print appName


    res = requests.get(BASE_URL + appUrl)
    soup = BeautifulSoup(res.text, "html.parser")
    content = res.text

    #print soup
    totInfo = soup.select('div.other-info p')[1:]
    #print len(totInfo)
    appType = ""
    appVersion = ""
    appUpdateTime = ""
    appSize = ""

    if len(totInfo) == 6:
        appType = totInfo[4].string[3:].strip().encode('utf8')
        appVersion = totInfo[2].string[3:].strip().encode('utf8')
        appUpdateTime = totInfo[1].string[3:].strip().encode('utf8')
        appSize = totInfo[0].string[3:].strip().encode('utf8')

    if len(totInfo) == 5:
        appType = totInfo[3].string[3:].strip().encode('utf8')
        appVersion = totInfo[1].string[3:].strip().encode('utf8')
        appSize = totInfo[0].string[3:].strip().encode('utf8')


    fout.write(CMD % (i, appName, appType, appVersion, appUpdateTime, appSize, appUrl, appIntro))

    #print totDetail
    totDetail = ""
    if len(soup.select('div.main-info p.art-content'))> 0:
        totDetail = soup.select('div.main-info p.art-content')[0].get_text()

    if len(totInfo) > 0:
        fItem = open('info/%d.txt' % i,'w')
        fItem.write(CMD % (i, appName, appType, appVersion, appUpdateTime, appSize, appUrl, appIntro))
        fItem.write(totDetail.encode('utf8'))
        fItem.close()
        time.sleep(2)


fout.close()
