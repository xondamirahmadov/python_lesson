n=int(input('n='))
T=[2]
for i in range(3,n*n+1,2):
    for j in T:
        if i%j==0:
            break
    else:
        T.append(i)
        if len(T)==n:
            break
print(T)