n = int(input())
if n == 0:
    print(0)
else:
    days = list(map(int, input().split()))
    money = 0
    for i in range(1, n):
        if days[i] > days[i - 1]:
            money += days[i] - days[i - 1]
    print(money)