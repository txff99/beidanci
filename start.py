import os
import random
import sys

words = list((i.strip('+') for i in open("unknownwords.txt",'r',encoding= 'UTF-8') if '+' in i))
means = list((i.strip('#') for i in open("unknownwords.txt",'r',encoding= 'UTF-8') if '#' in i))
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

f = open('unknownwords.txt', 'w', encoding='utf-8')
s = open('knownwords.txt', 'a', encoding='utf-8')
#unknown
random.shuffle(b)
b = b + [x for x in range(t, total)]
for i in b:
    wo = list(words[i])
    wo.insert(0,'+')
    f.write(''.join(wo))
    me = list(means[i])
    me.insert(0,'#')
    f.write(''.join(me))

#known
for i in a:
    wo = list(words[i])
    wo.insert(0,'+')
    s.write(''.join(wo))
    me = list(means[i])
    me.insert(0,'#')
    s.write(''.join(me))
f.close()
s.close()


