s=input()
A=set(s)
k=0
n='0'
for i in A:
    if s.count(i)>k:
        k=s.count(i)
        n=i
print(k,n)