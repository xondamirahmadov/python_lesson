s=input()
k=s.find("*")
f=s.find("=")
if k==-1 or f==-1:
    print("kiritish xatosi")
else:
    a=int(s[:k])
    b=int(s[k+1:f])
    c=int(s[f+1:])
    if a*b==c:
        print("To'g'ri")
    else:
        print("Xato")