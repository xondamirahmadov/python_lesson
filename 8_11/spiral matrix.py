def spiral_formula(n):
    A = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            k = min(i, j, n - 1 - i, n - 1 - j)
            m = n - 2 * k
            p = 4 * k * (n - k) + 1  # IMPORTANT

            if i == k:  # top
                A[i][j] = p + (j - k)
            elif j == n - 1 - k:  # right
                A[i][j] = p + (m - 1) + (i - k)
            elif i == n - 1 - k:  # bottom
                A[i][j] = p + 2 * m - 2 + (n - 1 - k - j)
            else:  # left
                A[i][j] = p + 3 * m - 3 + (n - 1 - k - i)

    return A
n=int(input())
A=spiral_formula(n)
for row in A:
    print(*row)