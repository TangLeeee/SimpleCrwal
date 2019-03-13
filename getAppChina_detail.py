import requests
from bs4 import BeautifulSoup
import time

BASE_URL = "http://www.appchina.com"

f = open('appchina.csv')

lines = f.readlines()

f.close()

for line in lines:
    tL = line.split(',')
    appName = tL[0]
    appUrl = tL[1]

    res = requests.get(BASE_URL + appUrl)

    soup = BeautifulSoup(res.text, "html.parser")
    #print soup
    totDetail = ""
    for item in soup.select('div.other-info p')[1:]:
        totDetail += item.get_text().strip() + '\n'

    totIntro = soup.select('div.main-info p.art-content')[0].string
    print totIntro

    exit()
