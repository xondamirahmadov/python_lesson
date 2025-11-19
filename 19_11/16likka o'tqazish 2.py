n=int(input())
s=[]
y=''
list='ABCDEF'
while n:
    x=n%16
    if x>9:
        y=list[x-10]
    else:
        y=str(x)
    s.append(y)
    n=n//16
s.reverse()
print("".join(s))