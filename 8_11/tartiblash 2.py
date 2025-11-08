A=list(map(int,input().split()))
s=[]
for j in range(len(A)):
    k = A[0]
    for i in range(len(A)):
        if A[i] < k:
            k = A[i]
    s.append(k)
    A.remove(k)
print(s)