n = int(input())  # Вводим размер массива
a = list(map(int, input().split()))  # Вводим массив

left = 0
right = n - 1

while left < right:
    mid = (left + right) // 2  # Середина массива
    if a[mid] < a[mid + 1]:
        left = mid + 1  # Ищем пик справа
    else:
        right = mid  # Ищем пик слева или в середине

# В конце left == right — это индекс пикового элемента
print(a[left])
