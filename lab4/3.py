import math

def phi(n):
    res = n
    limit = math.isqrt(n)  
    i = 2
    while i <= limit:
        if n % i == 0:
            while n % i == 0:
                n //= i
            res -= res // i
            limit = math.isqrt(n)
        i += 1

    if n > 1:
        res -= res // n

    return res

n = 36
print(f"Euler's totient function for {n} equals {phi(n)}")