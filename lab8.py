import random

def is_prime(n, k):
    if n < 2 or n % 2 == 0:
        return 0
    d = n - 1
    r = 0
    while d % 2 == 0:
        d >>= 1
        r += 1
    for i in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for j in range(r - 1):
            x = pow(x, 2, n)
            if x == 1:
                return False # бо 1
            if x == n - 1:
                continue
        return False  # складне
    return True  # просте

def generate_safe_prime(bit_length, iterations=5):
    while True:
        prime_candidate = random.getrandbits(bit_length - 1)
        prime_candidate |= (1 << (bit_length - 2)) | 1
        if is_prime(prime_candidate, iterations):
            safe_prime = 2 * prime_candidate + 1
            if is_prime(safe_prime, iterations):
                return safe_prime

def generate_primitive_root(prime_number):
    phi = prime_number - 1
    while True:
        candidate_root = random.randint(2, prime_number - 1)
        if pow(candidate_root, 2, prime_number) != 1 and pow(candidate_root, phi // 2, prime_number) != 1:
            return candidate_root

def diffie_hellman(bit_length=512):
    prime_modulus = generate_safe_prime(bit_length)
    primitive_root = generate_primitive_root(prime_modulus)
    print(f"Просте число: {prime_modulus}")
    print(f"Генератор: {primitive_root}")

    alice_private_key = random.randint(2, prime_modulus - 2)
    alice_public_key = pow(primitive_root, alice_private_key, prime_modulus)

    bob_private_key = random.randint(2, prime_modulus - 2)
    bob_public_key = pow(primitive_root, bob_private_key, prime_modulus)

    alice_shared_secret = pow(bob_public_key, alice_private_key, prime_modulus)
    bob_shared_secret = pow(alice_public_key, bob_private_key, prime_modulus)

    print(f"Приватний ключ Аліси: {alice_private_key}")
    print(f"Публічний ключ Аліси: {alice_public_key}")
    print(f"Приватний ключ Боба: {bob_private_key}")
    print(f"Публічний ключ Боба: {bob_public_key}")
    print(f"Секретний ключ Аліси: {alice_shared_secret}")
    print(f"Секретний ключ Боба: {bob_shared_secret}")
    print("Чи є ключ спільним? ", alice_shared_secret == bob_shared_secret)

diffie_hellman(bit_length=64)
