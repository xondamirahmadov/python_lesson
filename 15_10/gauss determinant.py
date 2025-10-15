def Gauss_usuli(A):
    n = len(A)
    f=1
    # To‘g‘ri yurish
    for i in range(n):
        if A[i][i] == 0:
            for k in range(i+1, n):
                if A[k][i] != 0:
                    A[i], A[k] = A[k], A[i]
                    break
        # Diagonal elementni 1 ga keltirish
        D = A[i][i]
        f=f*D
        for j in range(i, n):
            A[i][j] = A[i][j] / D

        # Pastdagi satrlardan i-chi noma'lumni yo‘qotish
        for k in range(i+1, n):
            koef = A[k][i]
            for j in range(i, n):
                A[k][j] -= koef * A[i][j]
    return f

print("Gauss usuli yordamida determinantni topish")
n = int(input("Matritsa o'lchami: "))
A = []
print("Matritsa elementlarini kiriting:")
for i in range(n):
    row = list(map(float, input().split()))
    A.append(row)
# Yechimni topish
x = Gauss_usuli(A)
print(x)
