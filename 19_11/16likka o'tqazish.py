n=int(input())
s=[]
y=''
while n:
    x=n%16
    if x==10:
        y="A"
    elif x==11:
        y="B"
    elif x==12:
        y="C"
    elif x==13:
        y="D"
    elif x==14:
        y="E"
    elif x==15:
        y="F"
    else:
        y=str(x)
    s.append(y)
    n=n//16
s.reverse()
print("".join(s))