def tub(n):
    s = 0
    for i in range(2, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            s = s + 1
            break
    if s == 0:
        return True;
    else:
        return False;
n=int(input("n sonini kiriting: "))
s=[]
i=0
a=2
while i<n:
    if tub(a):
        s=s+[a]
        i=i+1
    a=a+1
print(','.join(map(str, s)))