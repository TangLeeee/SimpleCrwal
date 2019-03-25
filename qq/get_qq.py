import requests
import json
from bs4 import BeautifulSoup
import time

BASE_URL = "https://sj.qq.com/myapp/cate/appList.htm?orgame=1&categoryId=116&pageSize=20&pageContext=%d"

res = requests.get(BASE_URL % 0)

step = 20

resFolder = 'info/'

fout = open('qq.csv','w')
CMD = '%d,%s,%s,%s,%s,%s,%d,%f\n'

num = 1

for i in range(20):
    print i
    pos = step * i
    res = requests.get(BASE_URL % pos)

    #print res.text
    dict_json = json.loads(res.content)
    for item in  dict_json['obj']:
        fout.write(CMD % (num,item['appName'].encode('utf8'),item['categoryName'].encode('utf8'),item['pkgName'].encode('utf8'),item['versionName'].encode('utf8'),item['authorName'].encode('utf8'),item['appDownCount'],item['averageRating']))

        ftmp = open(resFolder + item['pkgName'].encode('utf8') + '.txt','w')
        ftmp.write(item['newFeature'].encode('utf8') + '\n')
        ftmp.write(item['editorIntro'].encode('utf8'))
        ftmp.close()
        num += 1

fout.close()




