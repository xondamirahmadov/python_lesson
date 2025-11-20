n=int(input())
A=list(map(int,input().split()))
A.sort()
s=0
for i in A:
    for j in range(len(A)):
        if i%A[j]==0:
            s=s+1
print(s)



    # for j in A:
    #     if i%j==0:
    #         s=s+1
    # if s==n-1:
    #     print(j)
    # else:
    #     s=0