from math import cos, sin, pi
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
s=0
x=pi/3
n=1
i=1
p=(x**n)/fact(n)
for c in range(20):
    s=s+i*p
    n=n+2
    p=(x**n)/fact(n)
    i=-1*i
print("Teylor=",s)
print("ffsinx=",sin(x))