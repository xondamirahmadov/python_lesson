import time
n=int(input("enter a number: "))
s=0
a=time.time()
while n>=5:
    s=s+n//5
    n=n//5
b=time.time()
print(s)
print(b-a)