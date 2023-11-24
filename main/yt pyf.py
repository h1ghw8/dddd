s0=[]
with open('main/example_100kb.csv') as f:
    for line in f.readlines():
        s=line.strip().split(',')
        s0.append(s[2])
print(s0)
