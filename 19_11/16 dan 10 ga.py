n=input()
x=len(n)
s=0
list='ABCDEF'
for i in range(x):
    if n[i] in list:
        y=int(10+list.index(n[i]))
    else:
        y=int(n[i])
    s+=y*16**(x-i-1)
print(s)