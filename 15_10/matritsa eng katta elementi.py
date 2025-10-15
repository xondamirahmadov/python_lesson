n=int(input())
A=[]
for i in range(n):
    row=list(map(int,input().split()))
    A.append(row)
k=A[0][0]
for i in range(n):
    for j in range(n):
        if A[i][j]>k:
            k=A[i][j]
print(k)
