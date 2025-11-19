n=int(input())
s=[]
while n:
    s.append(str(n%2))
    n=n//2
s.reverse()
# s=str(s)
print("".join(s))