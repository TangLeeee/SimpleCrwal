# -- coding: utf-8 --

import os
import jieba
import re

toDict = {}
for item in os.listdir('info/'):
    with open('info/' + item) as fp:
        lines = fp.readlines()

    res_l = []
    for content in lines:
        seg_list = jieba.cut(content, cut_all=False)
        res_l += list(seg_list)

    for word in res_l:
        cur = word.strip()
        # 判断第一个字符是否为汉字，只输出汉字内容
        if cur >= u'\u4e00' and cur <= u'\u9fa5':
            if len(cur) >= 2:
                if cur in toDict:
                    toDict[cur] += 1
                else:
                    toDict[cur] = 1

toDict_sorted = sorted(toDict.items(), key=lambda x:x[1], reverse=True)
# print toDict_sorted


with open('fenci_huawei.csv', 'w') as fout:
    for item in toDict_sorted:
        # print item[0]
        # 格式化输出
        fout.write('{} : {}\n'.format(item[0].encode('utf8'), item[1]))