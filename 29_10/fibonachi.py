n=int(input())
a=[1,1]
for i in range(2,n):
    a.append(a[-1]+a[-2])
print(a)