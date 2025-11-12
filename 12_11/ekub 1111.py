a,b=map(str, input().split())
n=len(a)
m=len(b)
s=n*m
while m!=0:
    n,m=m,n%m
print("Ekub: "+"1"*n)
print("Ekuk: "+"1"*(s//n))