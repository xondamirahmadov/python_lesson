l=input()
n=len(l)
s=[]
alif='abcdefghijklmnopqrstuvwxyz'
for i in alif:
    if i in l:
        s.append(l.count(i))
        s.append(i)
for i in s:
    print(i,end="")