from math import cos, sin
s=0
eps=float(input("eps="))
n=1
i=1
p=1/n
while p>eps:
    s=s+p
    print(p, end="+")
    i=i+1
    n=n*i
    p=1/n
print("=",s)