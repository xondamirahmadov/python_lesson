# Gaussning noma'lumlarni ketma-ket yo'qotish usuli
# (Chiziqli algebraik tenglamalar sistemasini yechish)
def Gauss_usuli(A, b):
    n = len(A)
    # To‘g‘ri yurish
    for i in range(n):
        if A[i][i] == 0:
            for k in range(i+1, n):
                if A[k][i] != 0:
                    A[i], A[k] = A[k], A[i]
                    b[i], b[k] = b[k], b[i]
                    break
        # Diagonal elementni 1 ga keltirish
        D = A[i][i]
        for j in range(i, n):
            A[i][j] = A[i][j] / D
        b[i] = b[i] / D

        # Pastdagi satrlardan i-chi noma'lumni yo‘qotish
        for k in range(i+1, n):
            koef = A[k][i]
            for j in range(i, n):
                A[k][j] -= koef * A[i][j]
            b[k] -= koef * b[i]
    # Teskari yurish (noma'lumlarni topish)
    x = [0 for _ in range(n)]
    for i in range(n-1, -1, -1):
        x[i] = b[i]
        for j in range(i+1, n):
            x[i] -= A[i][j] * x[j]
    return x

print("Gauss usuli yordamida tenglamalar sistemasini yechish")
n = int(input("Tenglamalar sonini kiriting: "))
A = []
b = []
print("Tenglamalar sistemasi uchun koeffitsientlarni va ozod hadni kiriting:")
for i in range(n):
    row = list(map(float, input().split()))
    A.append(row[0:n])
    b.append(row[n])
# Yechimni topish
x = Gauss_usuli(A, b)
print("\nTenglamalar sistemasini yechimi:")
for i, val in enumerate(x, 1):
    print(f"x{i} = {val:.4f}")
