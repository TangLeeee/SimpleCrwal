import os
f = open('xiaomi.csv')
lines = f.readlines()
f.close()

for i in range(len(lines)):
    line = lines[i]
    package = line.strip().split(',')[1]
    os.rename('info/%d.txt' % i, 'info/%s.txt' % package)

