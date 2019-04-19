# -*- coding: utf-8 -*-  
import os
f = open('tot.csv')
lines = f.readlines()
f.close()

fout = open('targe.csv','w')

tarString = '阅后即焚'

for line in lines:
    tl = line.strip().split(',')
    appName = tl[0]
    package = tl[1]
    market = tl[2].split()

    if appName.find(tarString) >= 0:
        fout.write(line)
        continue

    for item in market:
        if os.path.exists('detail_info/%s/%s.txt' % (item, package)):
            f = open('detail_info/%s/%s.txt' % (item, package))
            content = f.read()
            f.close()

            if content.find(tarString) >= 0:
                fout.write(line)
                break
    
fout.close()


