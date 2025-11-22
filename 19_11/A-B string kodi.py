# a=input()
# b=input()
# if len(a)>len(b):
#     b=(len(a)-len(b))*'0'+b
# else:
#     a=(len(b)-len(a))*'0'+a
# r=""
# k=0
# for i in range(len(a)-1,-1,-1):
#     x=int(a[i])-k
#     y=int(b[i])
#     if x<y:
#         x+=10
#         k=1
#     else:
#         k=0
#     r=str(x-y)+r
# r=r.lstrip('0')
# if r=="":
#     r="0"
# print(r)

a=input()
b=input()
neg=False
if len(a)<len(b):
    neg=True
    a,b=b,a
elif len(a)==len(b):
    i=0
    while i<len(a):
        if a[i]>b[i]:
            break
        if a[i]<b[i]:
            neg=True
            a,b=b,a
            break
        i+=1
while len(b)<len(a):
    b="0"+b
r=""
q=0
list="0123456789"
i=len(a)-1
while i>=0:
    m=list.find(a[i])
    n=list.find(b[i])
    s= m - n - q
    if s<0:
        s+=10
        q=1
    else:
        q=0
    r=str(s)+r
    i-=1
while len(r)>1 and r[0]== "0":
    r= r[1:]
if neg:
    r= "-" + r
print(r)
