def Gauss_usuli(A):
    n = len(A)
    f = 1.0
    sanagich = 0

    # To‘g‘ri yurish
    for i in range(n):
        # Nolga teng diagonalni almashtirish
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

        # Diagonalni 1 ga keltirish
        for j in range(i, n):
            A[i][j] = A[i][j] / D

        # Pastdagi satrlardan yo‘qotish
        for k in range(i + 1, n):
            koef = A[k][i]
            for j in range(i, n):
                A[k][j] -= koef * A[i][j]

    det = f * (-1) ** sanagich
    return round(det, 6)  # natijani yaxlitlash

print("Gauss usuli yordamida determinantni topish")
n = int(input("Matritsa o'lchami: "))
A = []
print("Matritsa elementlarini kiriting:")
for i in range(n):
    row = list(map(float, input().split()))
    A.append(row)

# Yechimni topish
x = Gauss_usuli(A)
print("Determinant:", x)
