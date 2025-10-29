n=int(input())
l=''
for i in range(n+1):
    l=l+str(i)
    if l.find(str(n))>0:
        break
print(l.find(str(n)))