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
for i in range(2, n + 1):
    if tub(i):
        s=s+[i]
print(','.join(map(str, s)))