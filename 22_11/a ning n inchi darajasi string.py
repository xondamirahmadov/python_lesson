a=int(input())
n=int(input())
k=0
s="1"
for i in range(1,n+1):
    x=''
    k=0
    for j in range(len(s)-1,-1,-1):
        x=str((a*int(s[j])+k)%10)+x
        k=(a*int(s[j])+k)//10
    if k>0:
        x=str(k)+x
    s=x
print(s)
print(len(s))