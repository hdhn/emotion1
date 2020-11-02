f = open('mbox-short.txt', 'r', encoding='utf-8')
q ={}
for line in f:
    if not line.startswith("From"):
        continue
    elif not line.startswith("From:"):
        p=line.find(':')
        l=line[p-2:p]
        try:
            q[l]+=1
        except:
            q[l]=1
for k,v in sorted(q.items()):
    print(k,v)
