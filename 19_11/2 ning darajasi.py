def summa(a):
    k=0
    s=''
    for i in range(len(a)-1,-1,-1):
        y=2*int(a[i])+k
        s=str(y%10)+s
        k=y//10
    if k>0:
        s=str(k)+s
    return s

n=int(input())
s='1'
for i in range(n):
    s=summa(s)
print(s)
