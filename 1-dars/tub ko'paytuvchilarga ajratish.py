import time
a=int(input("a="))
s=[]
i=2
c=time.time()
while i<=a**(1/2):
    if a%i==0:
        s=s+[i]
        a=a//i
    else:
        i+=1
s=s+[a]
S=[str(n) for n in s]
b=time.time()
print('*'.join(S))
d=1
c=1
for i in range(1, len(s)):
    if s[i]==s[i-1]:
        c=c+1
    else:
        d=d*(c+1)
        c=1
d=d*(c+1)
print("bo'luvchilar soni:", d)
print(b-c)