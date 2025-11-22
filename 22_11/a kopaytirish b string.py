a=input()
n=int(input())
k=0
s="1"
x=''

for j in range(len(a)-1,-1,-1):
    x=str((n*int(a[j])+k)%10)+x
    k=(n*int(a[j])+k)//10
if k>0:
    x=str(k)+x
s=x
if n==0:
    print(0)
else:
    print(s)
