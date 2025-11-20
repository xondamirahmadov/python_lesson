n=input()
x=len(n)
s=0
for i in range(x):
    s+=int(n[i])*8**(x-i-1)
print(s)
