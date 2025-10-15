a=int(input())
s=[]
i=2
while i<=a**(1/2):
    if a%i==0:
        s=s+[i]
        a=a//i
    else:
        i+=1
s=s+[a]
A=set(s)
k=1
for i in A:
    k=k*(s.count(i))
print(k)