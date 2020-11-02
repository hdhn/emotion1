import matplotlib.pyplot as plt
RLIST = [0.33333]
DLIST = [0.33333]
ILIST = [0.33333]
for i in range(40):
    R = RLIST[i]*0.75 +DLIST[i]*0.2 +ILIST[i]*0.4
    RLIST.append(R)
    D = RLIST[i]*0.05 + DLIST[i]*0.60 +ILIST[i]*0.20
    DLIST.append(D)
    I = RLIST[i]*0.20+DLIST[i]*0.20 +ILIST[i]*0.40
    ILIST.append(I)
plt.plot(RLIST)
plt.plot(DLIST)
plt.plot(ILIST)
plt.xlabel('Time')
plt.ylabel('Voting percent')
plt.annotate('DemoccraticParty',xy = (5,0.2))
plt.annotate('RepublicanParty',xy = (5,0.5))
plt.annotate('IndeoendentCandidate',xy = (5,0.25))
plt.show()
print(RLIST,DLIST,ILIST)
