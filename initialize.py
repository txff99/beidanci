#coding=utf-8

import os


lines = list(i for i in open("test.txt",'r',encoding= 'UTF-8') if '#' in i or '+' in i)
f = open('unknownwords.txt', 'w', encoding='utf-8')
lines_new=[]
k=-1
for i in lines:
    print(i)
    if '+' in i:
        j=0
        lines_new.append(i)
    else:
        j=j+1
        if j!=1:
            lines_new[-1]=lines_new[-1].strip('\n')+i
        else:
            lines_new.append(i)


    

f.writelines(lines_new)
f.close()





    
#lines = (i for i in open('test.txt', 'rb') if '+' in i)
#f = open('test_new.txt','w', encoding="utf-8")
#f.writelines(lines)
#f.close()
