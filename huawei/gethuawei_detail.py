import re
import time
from bs4 import BeautifulSoup
import requests

BASE_URL = 'http://app.hicloud.com'
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

with open('huawei.csv', 'r') as f:
    lines = f.readlines()

for line in lines:
    content = line.split(' ')
    appUrl = content[0]
    appName = content[1]

    res = requests.get(BASE_URL + appUrl, headers=headers)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    item = soup.select('div.content div#app_desc')[0].get_text()
    # print item

    txtName = appUrl[5:]
    with open('info/%s.txt' % txtName, 'a') as fout:
        fout.write(item.encode('utf-8'))

