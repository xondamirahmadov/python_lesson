n=int(input())
s=[]
for i in range(1,n):
    if n%i==0:
        s.append(i)
print(s)
