import time, random

a = random.randrange(10,1000000)
arr = [random.randrange(1,1000) for _ in range(a)]

def testTime(fn):
    def time_func(*args):
        st = time.time()
        fn(*args)
        dt = time.time() - st
        return dt
    return time_func

@testTime
def chek_arr(arr1):
    count = 0
    for i in arr1:
        count += 1
    return count

print(f"Функция подсчитала размер массива (с длинной {len(arr)}) за {chek_arr(arr)} секунд") 