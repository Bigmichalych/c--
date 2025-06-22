def backtrack(n, start, path):
    if n == 0:
        print(*path)
        return
    for i in range(start, n + 1):
        backtrack(n - i, i, path + [i])

n = int(input())
backtrack(n, 1, [])
