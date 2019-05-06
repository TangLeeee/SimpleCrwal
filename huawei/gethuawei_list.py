import requests, chardet
from bs4 import BeautifulSoup
import time

BASE_URL = 'http://app.hicloud.com/soft/list_26_1_%d'
# fake headers avoid being forbidden
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

with open('huawei.csv', 'w',) as fout:
    for i in range(1, 10):
        print i, BASE_URL % i

        res = requests.get(BASE_URL % i, headers=headers)
        # here need to set encoding!!! waste a lot of time
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text, 'html.parser')
        for item in soup.select('div.unit-main h4.title a'):
            appUrl = item['href']
            appName = item.string

            fout.write('{} {}\n'.format(appUrl.encode('utf8'), appName.encode('utf8')))

        time.sleep(2)

    print 'write complete!'
