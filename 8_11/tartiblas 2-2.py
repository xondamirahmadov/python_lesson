A=list(map(int,input().split()))
for j in range(len(A)):
    for i in range(len(A)-1):
        if A[i] < k:
            k = A[i]
print(A)