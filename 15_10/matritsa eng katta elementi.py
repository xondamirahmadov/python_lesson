n=int(input())
m=int(input())
A=[]
for i in range(n):
    row=list(map(int,input().split()))
    A.append(row)
s=[]
for i in range(n):
    f=A[i][0]
    for j in range(m):
        if A[i][j]>f:
            f=A[i][j]
    print(f"{i+1}-satrdagi eng katta elementi {f}")

