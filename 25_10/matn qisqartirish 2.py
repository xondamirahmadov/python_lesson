s=input()
k=1
l=""
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        k=k+1
    else:
        l=l+str(k)+s[i]
        k=1
l=l+str(k)+s[-1]
print(l)
