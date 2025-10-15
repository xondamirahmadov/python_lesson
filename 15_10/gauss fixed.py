# Gaussning noma'lumlarni ketma-ket yo'qotish usuli
# (Chiziqli algebraik tenglamalar sistemasini yechish)

def Gauss_usuli(A, b):
    n = len(A)

    for i in range(n):
        # Nol diagonal elementni almashtirish
        if A[i][i] == 0:
            for k in range(i + 1, n):
                if A[k][i] != 0:
                    A[i], A[k] = A[k], A[i]
                    b[i], b[k] = b[k], b[i]
                    break

        # Agar almashtirgandan keyin ham nol bo'lsa — bu o‘rinda yechim aniqlanmaydi
        if A[i][i] == 0:
            continue  # keyingi satrga o‘tish (tekshiruv keyin bo‘ladi)

        # Diagonalni 1 ga keltirish
        D = A[i][i]
        for j in range(i, n):
            A[i][j] = A[i][j] / D
        b[i] = b[i] / D

        # Pastdagi satrlardan yo‘qotish
        for k in range(i + 1, n):
            koef = A[k][i]
            for j in range(i, n):
                A[k][j] -= koef * A[i][j]
            b[k] -= koef * b[i]

    # Rank aniqlash (A va [A|b] uchun)
    rank_A = 0
    rank_Ab = 0
    for i in range(n):
        # faqat nol bo'lmagan satrlarni sanash
        if any(abs(val) > 1e-9 for val in A[i]):
            rank_A += 1
        if any(abs(val) > 1e-9 for val in A[i]) or abs(b[i]) > 1e-9:
            rank_Ab += 1

    # Tahlil
    if rank_A < rank_Ab:
        print("❌ Sistema yechimga ega emas (no solution).")
        return None
    elif rank_A < n:
        print("♾ Sistema cheksiz ko‘p yechimga ega (infinite solutions).")
        return None

    # Teskari yurish (noma'lumlarni topish)
    x = [0 for _ in range(n)]
    for i in range(n - 1, -1, -1):
        x[i] = b[i]
        for j in range(i + 1, n):
            x[i] -= A[i][j] * x[j]

    return x


# === Asosiy dastur ===
print("Gauss usuli yordamida tenglamalar sistemasini yechish")
n = int(input("Tenglamalar sonini kiriting: "))
A = []
b = []
print("Tenglamalar sistemasi uchun koeffitsientlarni va ozod hadni kiriting:")
for i in range(n):
    row = list(map(float, input().split()))
    A.append(row[0:n])
    b.append(row[n])

x = Gauss_usuli(A, b)

if x is not None:
    print("\n✅ Tenglamalar sistemasining yagona yechimi:")
    for i, val in enumerate(x, 1):
        print(f"x{i} = {val:.6f}")
