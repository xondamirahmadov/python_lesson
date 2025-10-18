from math import cos, sin, pi
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
s=0
eps=float(input("eps="))
x=pi/3
n=0
i=1
p=1
t=1
while p>eps:
    s=s+i*p
    n=n+2
    t=t*x*x
    p=t/fact(n)
    i=-1*i
print("Teylor=",s)
print("ffcosx=",cos(x))
print("xatolik=",s-cos(x))