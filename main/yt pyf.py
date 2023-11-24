s0=[]
with open('main/example_100kb.csv') as f:
    for line in f.readlines():
        s=line.strip().split(',')
        s0.append(s[2])
s1=set()
l=''
for i in range(1, len(s0), 2):
    temp, k=s0[i].split('@')
    s1.add(k)
    l+=k
s2=[]
for j in s1:
    s2.append(l.count(j))
n_s2, n_s1=zip(*[(b,a) for b,a in sorted(zip(s2,s1))])
import csv
with open('new.csv', 'w', newline='') as csvfile:
    filewriter=csv.writer(csvfile, delimiter=',',
    quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['domen', 'count'])
    for x in range(len(n_s1)-1,-1,-1):
        filewriter.writerow([n_s1[x], n_s2[x]])
