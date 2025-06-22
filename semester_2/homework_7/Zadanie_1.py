import math

def catalan_number(n):
    numerator = math.factorial(2 * n)         # (2n)!
    denominator = math.factorial(n + 1) * math.factorial(n)  # (n+1)! * n!
    return numerator // denominator        

n = int(input())
print(catalan_number(n))
