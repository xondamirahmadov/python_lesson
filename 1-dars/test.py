import time
n=int(input())
s=0
a=time.time()
for i in range(2,int(n**(1/2))+1):
    if n%i==0:
        s=s+1
        break
b=time.time()
if n==1:
    print("Tub ham murakkab ham emas")
else:
    if s==0:
        print("Tub")
    else:
        print("Tub emas")
print(b-a)