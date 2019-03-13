f = open('test.html')
lines = f.readlines()
f.close()
print lines[514]
fout = open('test2','w')
fout.write(lines[514])
fout.close()
