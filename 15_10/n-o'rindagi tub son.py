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
i=1
a=3
if n==1:
    print(2)
else:
    while i<n:
        if tub(a):
            i=i+1
        a=a+2
    print(a-2)