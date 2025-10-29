def tub(n):
    s = 0
    for i in range(2, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            s = s + 1
            break
    if s == 0:
        return True
    else:
        return False
n=list(map(int, input().split()))
a=n[0]
for i in n:
    if tub(i):
        if i>a:
            a=i
if tub(a):
    print(a)
else:
    print("Tub son yo'q")