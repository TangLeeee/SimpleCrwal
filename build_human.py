f = open('human_done.csv')
lines = f.readlines()
f.close()

fout = open('done.csv','w')

for line in lines:
    tl = line.strip().split(',')
    packName = tl[0]
    fout.write(tl[0] + ',original\n')

fout.close()