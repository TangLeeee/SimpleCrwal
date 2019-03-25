import os
import jieba
totDict = {}
for item in os.listdir('info/'):
    print item
    f = open('info/' + item)
    lines = f.readlines()
    f.close()
    content = lines[1]

    seg_list = jieba.cut(content, cut_all=False)
    l = list(seg_list)
    for tWord in l:
        cur = tWord.strip()
        if len(cur) >= 2:
            if totDict.has_key(cur):
                totDict[cur] += 1
            else:
                totDict[cur] = 1
fout = open('word.csv','w')
for key in totDict:
    fout.write('%s,%d\n' % (key.encode('utf8'), totDict[key]))
fout.close()
