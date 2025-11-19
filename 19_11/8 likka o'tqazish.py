n=int(input())
s=[]
while n:
    s.append(str(n%8))
    n=n//8
s.reverse()
print("".join(s))