fdone = open('done.csv')
lines = fdone.readlines()
fdone.close()


doneSet = set()
for line in lines:
    tl = line.strip().split(',')
    packName = tl[0]
    doneSet.add(packName)    

#print doneSet

fin = open('appchina/appchina_handout.csv')
lines = fin.readlines()
fin.close()

fout = open('undone.csv','w')

for line in lines:
    tl = line.strip().split(',')
    packName = tl[0]
    print packName
    if packName in doneSet:
        continue
    fout.write(line)

fout.close()
