n=int(input())
x=1
for i in range(1,n+1):
    x=x*i
a=0
while 1:
    a=(x//10)%10
    if a!=0:
        break
    else:
        x=x//10
print(a)