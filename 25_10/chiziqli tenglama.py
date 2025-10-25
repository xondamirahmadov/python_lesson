s=input()
k=s.find("x")
e=s.find("=")
a=int(s[:k])
b=int(s[k+1:e])
c=int(s[e+1:])
if a==0 and b==c:
    print("Cheksiz ko'p yechim")
elif a==0 and b!=c:
    print("Yechim mavjud emas")
else:
    x=(c-b)/a
    print(x)