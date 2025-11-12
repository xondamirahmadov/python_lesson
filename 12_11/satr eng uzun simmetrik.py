def sim(s):
    c = s[::-1]
    if c==s:
        return True
    else:
        return False
s=input()
n=len(s)
k=0
b=''
for i in range(n):
    for j in range(i,n):
        if sim(s[i:n-j]):
            if len(s[i:n-j])>k:
                k=len(s[i:n-j])
                b=s[i:n-j]
print(b)