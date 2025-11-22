# def onlik(n,k):
#     x = len(n)
#     s = 0
#     list = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     for i in range(x):
#         y = int(list.index(n[x-i-1]))
#         s +=(y * k ** i)
#     return s
# k,m=map(int,input().split())
# n=input()
# print(onlik(n,k)%m)
#
def onlik_mod(n, k, m):
    list = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    rem = 0
    for ch in n:
        val = list.index(ch)
        rem = (rem * k + val) % m
    return rem

k, m = map(int, input().split())
n = input().strip()
print(onlik_mod(n, k, m))
