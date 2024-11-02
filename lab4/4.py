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

def inverse_element_2(a, n):
    phi_n = phi(n)
    return pow(a, phi_n - 1, n)


a = 5
n = 18
inverse = inverse_element_2(a, n)
print(f"Modular inverse of {a} mod {n} is {inverse}")
print(f"Test: ({a} * {inverse}) % {n} = {(a * inverse) % n}")