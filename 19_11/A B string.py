a=input("a=")
b=input("b=")
d=''
n=len(a)
m=len(b)
x=abs(n-m)
for i in range(x):
    d=d+'0'
if n<m:
    a=d+a
else:
    b=d+b
print(a,b)
s=''
k=0
for i in range(len(a)-1,-1,-1):
    y=int(a[i])+int(b[i])+k
    s=str(y%10)+s
    k=y//10
if k>0:
    s=str(k)+s
print(s)