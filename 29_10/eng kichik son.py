n=input()
a=[]
for i in n:
    a.append(int(i))
a.sort()
b=1
for i in a:
    if i!=0:
        b=i
        break
a.remove(b)
print(b,end='')
for i in a:
    print(i,end='')


