import random

def miller_rabin(n, k):
    if n % 2 == 0:
        return False
    
    m = n - 1
    t = 1
    while m % 2 == 0:
        m //= 2
        t += 1
    
    for _ in range(k):
        a = random.randint(2, n - 2)
        u = pow(a, m, n)
        if u == 1:
            continue
        j = 1
        
        while u != n - 1 and j < t:
            u = pow(u, 2, n)
            if u == 1:
                return False # бо 1
            j += 1
        
        if u != n - 1:
            return False
    
    return True


n = 13  
k = 25  
is_prime = miller_rabin(n, k)
print(f"Is {n} prime? {is_prime}")