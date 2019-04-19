

f1 = open('appchina.csv')
lines = f1.readlines()
f1.close()

appDict = {}

for line in lines:
    tl = line.strip().split(',')

    package = tl[1][5:]
    appName = tl[0]
    if appDict.has_key(package):
        appDict[package][1] .append('appchina')
    else:
        appDict[package] = [appName, ['appchina']]

f2 = open('qq_shejiao.csv')
lines = f2.readlines()
f2.close()

for line in lines:
    tl = line.strip().split(',')

    package = tl[3]
    appName = tl[1]
    if appDict.has_key(package):
        appDict[package][1] .append('qq')
    else:
        appDict[package] = [appName, ['qq']]
   
f2 = open('qq_tongxun.csv')
lines = f2.readlines()
f2.close()

for line in lines:
    tl = line.strip().split(',')

    package = tl[3]
    appName = tl[1]
    if appDict.has_key(package):
        appDict[package][1] .append('qq')
    else:
        appDict[package] = [appName, ['qq']]

f2 = open('xiaomi.csv')
lines = f2.readlines()
f2.close()

for line in lines:
    tl = line.strip().split(',')

    package = tl[1]
    appName = tl[0]
    if appDict.has_key(package):
        appDict[package][1] .append('xiaomi')
    else:
        appDict[package] = [appName, ['xiaomi']]

fout = open('tot.csv','w')
for item in appDict.keys():
    appName = appDict[item][0]
    package = item
    cates = ' '.join(appDict[item][1])
    fout.write('%s,%s,%s\n' % (appName, package, cates))
fout.close()
    