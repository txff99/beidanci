import os
import random
import sys

words = list((i.strip('+') for i in open("knownwords.txt",'r',encoding= 'UTF-8') if '+' in i))
means = list((i.strip('#') for i in open("knownwords.txt",'r',encoding= 'UTF-8') if '#' in i))
total = len(words)
print("unknown words left: ",total)
t = int(input("input a number: "))
if t>total:
    print("number too big")
    sys.exit()
a=[]
b=[]
for i in range(0,t):
    print(words[i])
    comm = input("sibuside(y/n)")
    if comm == 'y':
        a.append(i)
    else:
        b.append(i)
    print(means[i])
print(a)

f = open('unknownwords.txt', 'r', encoding='utf-8')
shit = f.readlines()
f.close()
s = open('knownwords.txt', 'w', encoding='utf-8')
f = open('unknownwords.txt', 'w', encoding='utf-8')
#unknown
random.shuffle(b)

for i in b:
    me = list(means[i])
    me.insert(0,'#')
    
    wo = list(words[i])
    wo.insert(0,'+')
    f.write(''.join(wo))
    f.write(''.join(me))
    
f.writelines(shit)   

#known
a = a + [x for x in range(t, total)]
for i in a:
    wo = list(words[i])
    wo.insert(0,'+')
    s.write(''.join(wo))
    me = list(means[i])
    me.insert(0,'#')
    s.write(''.join(me))
f.close()
s.close()
