fin = open('word.csv')
lines = fin.readlines()
fin.close()
tmpL = []

for line in lines:
    tl = line.strip().split(',')
    tmpL.append((tl[0],int(tl[1])))

res = sorted(tmpL, key=lambda x:x[1], reverse=True)
fout = open('word_sorted.csv','w')
for item in res:
    fout.write("%s,%d\n" % item)
fout.close()
