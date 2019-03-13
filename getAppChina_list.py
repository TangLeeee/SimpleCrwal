import requests
from bs4 import BeautifulSoup
import time

BASE_URL = "http://www.appchina.com/category/308/1_1_%d_1_0_0_0.html"

fout = open('appchina.csv','w')

for i in range(1,35):
    print i

    res = requests.get(BASE_URL % i)
    soup = BeautifulSoup(res.text, "html.parser")
    for item in soup.select('ul.app-list li'):
        appUrl = item.select('h1.app-name a')[0]['href']
        appName = item.select('h1.app-name a')[0].string
        appIntro = item.select('div.app-intro span')[0].string
        if not appIntro:
            appIntro = ""
        fout.write('%s,%s,"%s"\n' % (appName.encode('utf8'), appUrl.encode('utf8'), appIntro.encode('utf8')))

    time.sleep(5)

fout.close()
