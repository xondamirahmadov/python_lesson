A=[]
A=list(map(int,input().split()))
x=A[0]
n=1
for k in A:
    if k>x:
        x=k
        n+=1
print(f"Eng kattasi {x}, u to'plamning {n}-elementi")