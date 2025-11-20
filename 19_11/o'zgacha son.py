n=int(input())
A=list(map(int,input().split()))
A.sort()
s=0
l=[]
for i in A:
    s=0
    for j in A:
        if j%i==0:
            s=s+1
    l.append(s)
print(l)
print(A)
if n-1 in l:
    print(A[l.index(n-1)])
else:
    print("Mavjud emas")