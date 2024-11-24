import random

def miller_rabin(n, k=5):
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
                return False
            j += 1
        if u != n - 1:
            return False
    return True

def generate_safe_prime(bits=16):
    while True:
        q = random.getrandbits(bits - 1)
        q |= (1 << (bits - 2)) | 1
        if miller_rabin(q):
            p = 2 * q + 1
            if miller_rabin(p):
                return p

def generate_primitive_root(prime):
    phi = prime - 1
    while True:
        potential_root = random.randint(2, prime - 1)
        if pow(potential_root, 2, prime) != 1 and pow(potential_root, phi // 2, prime) != 1:
            return potential_root


def diffie_hellman_exchange():
    bits = 32
    p = generate_safe_prime(bits)
    g = generate_primitive_root(p)
    print(f"Generated safe prime p: {p}")
    print(f"Primitive root g: {g}")
    a = random.randint(2, p - 2)
    b = random.randint(2, p - 2)
    print(f"Alice's secret key (a): {a}")
    print(f"Bob's secret key (b): {b}")
    A = pow(g, a, p)
    B = pow(g, b, p)
    print(f"Alice's public key (A): {A}")
    print(f"Bob's public key (B): {B}")
    shared_key_alice = pow(B, a, p)
    shared_key_bob = pow(A, b, p)
    print(f"Alice's shared key: {shared_key_alice}")
    print(f"Bob's shared key: {shared_key_bob}")
    assert shared_key_alice == shared_key_bob, "Shared keys do not match!"
    print("Shared key exchange successful!")
    return shared_key_alice

shared_key = diffie_hellman_exchange()
print(f"Shared secret key: {shared_key}")
