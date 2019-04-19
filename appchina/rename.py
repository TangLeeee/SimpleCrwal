import os
f = open('appchina.csv')
lines = f.readlines()
f.close()

for i in range(len(lines)):
    line = lines[i]
    package = line.strip().split(',')[1][5:]
    if os.path.exists('info/%d.txt' % i):
        os.rename('info/%d.txt' % i, 'info/%s.txt' % package)

