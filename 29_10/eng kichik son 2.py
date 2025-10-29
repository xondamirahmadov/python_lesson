n=input()
a=[]
for i in n:
    a.append(int(i))
a.sort()
x=0
for i in range(len(a)):
    if a[i]!=0:
        x=i
        break
a[0],a[x]=a[x],a[0]
for i in a:
    print(i,end='')