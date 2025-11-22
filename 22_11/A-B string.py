a=input()
b=input()
katta=True
if len(a)>=len(b):
    b=(len(a)-len(b))*'0'+b
else:
    a=(len(b)-len(a))*'0'+a
if a<b:
    a,b=b,a
    katta=False
# if katta:
#     print(a)
# else:
#     print(b)
s=''
q=0
if a==b:
    print('0')
else:
    for i in range(len(a)-1,-1,-1):
        x=int(a[i])-int(b[i])-q
        if x<0:
            x=x+10
            q=1
        else:
            q=0
        s=str(x)+s
    while s[0]=='0':
            s=s[1:]
    if not katta:
        s = '-' + s
    print(s)

