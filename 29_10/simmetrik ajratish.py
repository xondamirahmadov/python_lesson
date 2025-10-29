def sim(n):
    b=''
    n=str(n)
    for i in range(len(n)-1,-1,-1):
        b=b+n[i]
    if int(n)==int(b):
        return True
    else:
        return False
n=list(map(int,input().split()))
for i in n:
    if sim(i):
        print(i, end=' ')