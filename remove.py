

readfile = open('knownwords.txt','r',encoding='utf-8')
lines_seen = set()
for line in readfile:
 #   line = line.strip('\n')
    if line not in lines_seen:
        lines_seen.add(line)
readfile.close()
outfile = open('knownwords.txt','w',encoding='utf-8')
for line in lines_seen:
    outfile.write(line)
outfile.close()