f=open('test.xml','w')
f.write('<?xml version="1.0" standalone="yes"?>\n')
f.write('<articleList>\n')
times=1000000
index=0
while index<times:
    f.write('  <article>\n')
    f.write('    <id>'+str(10000+index)+'</id>\n')
    f.write('</article>\n')
    index=index+1
f.write('</articleList>')
f.close()

import os
print("generate ok!")
os.system('pause')
