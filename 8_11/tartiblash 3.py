A=list(map(int,input().split()))
for j in range(len(A)):
    for i in range(j,0,-1):
        if A[i] < A[i-1]:
            A[i],A[i-1] = A[i-1],A[i]
    print(A)

# A=list(map(int, input().split()))
# n=len(A)
# for i in range(n-1):
#     for j in range(n-1-i):
#         if A[j]>A[j+1]:
#             A[j],A[j+1]=A[j+1],A[j]
#     print(A)
