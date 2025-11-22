a=input()
b=input()
if len(a)>len(b):
    b=(len(a)-len(b))*'0'+b
else:
    a=(len(b)-len(a))*'0'+a
list="0123456789ABCDEF"
k=""
m=0
for i in range(len(a)-1,-1,-1):
    x=list.index(a[i])
    y=list.index(b[i])
    s=x+y+m
    k=list[s%16]+k
    m=s//16
if m>0:
    k=list[m]+k
print(k)