from random import randint
import pycosat

K = -1


def get(v, i, j):
    global K
    return (v * K * K + i * K + j + 1)


def mySol():
    global K
    n = randint(1, 20)
    m = randint(1, 20)
    q = randint(0, n * m - 1)

    # n, m = map(int, input().split())
    K = max(n, m)
    # q = int(input())
    a = []
    for i in range(q):
        ai1 = randint(1, n * m)
        ai2 = randint(1, n * m)
        if ai2 == ai1:
            ++ai2
            if (ai2 > n * m):
                ai2 = 1
        # ai1, ai2 = map(int, input().split())
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
        return
        # print("No solution((")
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
        cnt = [False for i in range(n * m)]
        for i in range(n):
            for j in range(m):
                val = pans[i][j] - 1
                if cnt[val]:
                    print("ERROR1")
                    print(n, m)
                    print(q)
                    for (v, u) in a:
                        print(v + 1, u + 1)
                    exit()
                cnt[val] = True
        for i in range(n * m):
            if (not cnt[i]):
                print("ERROR2")
                print(n, m)
                print(q)
                for (v, u) in a:
                    print(v + 1, u + 1)
                exit()
        for (v, u) in a:
            for i in range(n):
                for j in range(m):
                    if (pans[i][j] == v+1):
                        for (di, dj) in mv:
                            ni = i + di
                            nj = j + dj
                            if (ni < 0 or nj < 0 or n <= ni or m <= nj): continue
                            if (pans[ni][nj] == u+1):
                                print("ERROR3")
                                print(n, m)
                                print(q)
                                for (v, u) in a:
                                    print(v + 1, u + 1)
                                exit()
                    elif (pans[i][j] == u + 1):
                        for (di, dj) in mv:
                            ni = i + di
                            nj = j + dj
                            if (ni < 0 or nj < 0 or n <= ni or m <= nj): continue
                            if (pans[ni][nj] == v + 1):
                                print("ERROR4")
                                print(n, m)
                                print(q)
                                for (v, u) in a:
                                    print(v+1, u+1)
                                exit()
    print("Ok")


for i in range(100):
    print("testNum=", i)
    mySol()
