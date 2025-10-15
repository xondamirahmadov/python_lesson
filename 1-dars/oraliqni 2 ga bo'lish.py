import math
def f(x):
    return (math.exp(x)-math.tan(x));
a,b=map(int,input().split())
e=float(input())
s=0
while (abs(f(a))>=e):
    t=(a+b)/2
    if f(a)*f(t)<0:
        b=t
    else:
        a=t
    s=s+1
print(a, abs(f(a)), s)