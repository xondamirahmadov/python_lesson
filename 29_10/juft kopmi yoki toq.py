def juft(n):
    if n%2==0:
        return True
    else:
        return False
n=list(map(int,input().split()))
a=0
for i in n:
    if juft(i):
        a=a+1
b=len(n)-a
if a>b:
    print("juft sonlar")
elif a<b:
    print("toq sonlar")
else:
    print("teng")