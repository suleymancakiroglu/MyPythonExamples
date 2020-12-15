"""
Break and continue terms are used in loop. The break term used just for stopped in self loop.
"""
i=0
while (i<20):
    print(i)
    if (i==5):
        break
    i += 1
"""
If loop anywhere encounter with continue term it will be returns to the beginning without coming down.
"""
liste=[1,2,3,4,5,6]
for i in liste:
    if(i==3 or i==5):
        continue
    print("i :",i)