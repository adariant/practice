import pycosat


def get(v, i, j):
    return (v * K * K + i * K + j + 1)


n, m = map(int, input().split())
K = max(n, m)
q = int(input())
a = []
for i in range(q):
    ai1, ai2 = map(int, input().split())
    ai1 -= 1
    ai2 -= 1
    a.append([ai1, ai2])

cnf = []
k = n * m
# at least once
for v in range(k):
    cur = []
    for i in range(n):
        for j in range(m):
            cur.append(get(v, i, j))
    cnf.append(cur)

# at most once
for v in range(k):
    for u in range(v + 1, k):
        for i in range(n):
            for j in range(m):
                cnf.append([-get(v, i, j), -get(u, i, j)])

# extra if
mv = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
for (v, u) in a:
    for i in range(n):
        for j in range(m):
            for (di, dj) in mv:
                ni = i + di
                nj = j + dj
                if (ni < 0 or nj < 0 or n <= ni or m <= nj): continue
                cnf.append([-get(v, i, j), -get(u, ni, nj)])
                # cnf.append([-get(u, i, j), -get(v, ni, nj)])

# print(*cnf)
ans = pycosat.solve(cnf)
# print(*ans)
if isinstance(ans, str):
    print("No solution")
else:
    pans = [[0 for j in range(m)] for i in range(n)]
    for v in range(k):
        for i in range(n):
            for j in range(m):
                num = get(v, i, j)
                num -= 1
                if (ans[num] > 0):
                    # print(v, i, j)
                    pans[i][j] = v + 1
    for i in range(n):
        print(*pans[i])
