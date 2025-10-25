s=input()
k=s.find("x")
e=s.find("=")
if k==0:
    a=1
elif s[:k]=='-':
    a=-1
else:
    a=int(s[:k])
b=int(s[k+1:e])
c=int(s[e+1:])
if a==0 and b==c:
    print("Cheksiz ko'p yechim")
elif a==0 and b!=c:
    print("Yechimga ega emas")
else:
    x=(c-b)/a
    print(x)