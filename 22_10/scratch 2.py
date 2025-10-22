from copy import deepcopy


def deter(A):
    n = len(A)
    f = 1.0
    sanagich = 0
    A = [row[:] for row in A]  # Asl matritsani o‘zgartirmaslik uchun nusxa

    for i in range(n):
        if A[i][i] == 0:
            for k in range(i + 1, n):
                if A[k][i] != 0:
                    A[i], A[k] = A[k], A[i]
                    sanagich += 1
                    break

        D = A[i][i]
        f *= D
        if D == 0:
            return 0  # determinant nol bo‘ladi

        for j in range(i, n):
            A[i][j] = A[i][j] / D

        for k in range(i + 1, n):
            koef = A[k][i]
            for j in range(i, n):
                A[k][j] -= koef * A[i][j]

    det = f * (-1) ** sanagich
    return round(det, 6)

print("Kramer usuli yordamida tenglamalar sistemasini yechish")
n = int(input("Tenglamalar sonini kiriting: "))
A = []
b = []

print("Tenglamalar sistemasi uchun koeffitsientlarni va ozod hadni kiriting:")
for i in range(n):
    row = list(map(float, input().split()))
    A.append(row[0:n])
    b.append(row[n])
dA = deter(A)
if dA == 0:
    print("Yechim yo‘q yoki cheksiz yechim bor.")
else:
    x = []
    for i in range(n):
        Ai = deepcopy(A)
        for j in range(n):
            Ai[j][i] = b[j]
        di = deter(Ai)
        x.append(di/dA)
print(x)
