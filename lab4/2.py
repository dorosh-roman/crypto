
def gcdex(a, b):
    x0 = 1
    y0 = 0
    x1 = 0
    y1 = 1    
    while b != 0:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return x0, y0, a

def inverse_element(a, n):
    x, y, gcd = gcdex(a, n)

    if gcd != 1:
        return None  
    else:
        return x % n

a = 5
n = 18
inverse = inverse_element(a, n)
if inverse is not None:
    print(f"Modular inverse of {a} mod {n} is {inverse}.")
    print(f"Test: ({a} * {inverse}) % {n} = {(a * inverse) % n}")
else:
    print(f"Modular inverse of {a} mod {n} doesnt exist")