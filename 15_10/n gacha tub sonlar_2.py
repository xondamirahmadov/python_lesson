n=int(input('n='))
T=[2]
for i in range(3,n+1,2):
    for j in T:
        if i%j==0:
            break
    else:
        T.append(i)
print(T)
print(len(T))