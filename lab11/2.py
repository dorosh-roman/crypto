import random

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

def modular_inverse(a, n):
    x, y, gcd = gcdex(a, n)

    if gcd != 1:
        return None  
    else:
        return x % n

def select_random_point(a, b, mod):
    while True:
        x = random.randint(0, mod - 1)
        y = random.randint(0, mod - 1)
        if pow(y, 2, mod) == (pow(x, 3, mod) + a * x + b) % mod:
            return x, y

def elliptic_addition(p1, p2, a_coeff, modulus):
    if p1 == (None, None):
        return p2
    if p2 == (None, None):
        return p1
    if p1[0] == p2[0] and p1[1] != p2[1]:
        return None, None

    if p1 == p2:
        slope = (3 * pow(p1[0], 2, modulus) + a_coeff) * modular_inverse(2 * p1[1], modulus) % modulus
    else:
        slope = (p2[1] - p1[1]) * modular_inverse((p2[0] - p1[0]), modulus) % modulus

    x3 = (pow(slope, 2, modulus) - p1[0] - p2[0]) % modulus
    y3 = (slope * (p1[0] - x3) - p1[1]) % modulus
    return x3, y3

def elliptic_multiply(point, scalar, a_coeff, modulus):
    result = (None, None)
    temp_point = point

    while scalar > 0:
        if scalar % 2 == 1:
            result = elliptic_addition(result, temp_point, a_coeff, modulus)
        temp_point = elliptic_addition(temp_point, temp_point, a_coeff, modulus)
        scalar //= 2

    return result

def calculate_order(point, a_coeff, modulus):
    order = 1
    temp = point
    while temp != (None, None):
        temp = elliptic_addition(temp, point, a_coeff, modulus)
        order += 1
    return order

def generate_keys(base_point, a_coeff, modulus):
    order = calculate_order(base_point, a_coeff, modulus)
    private_key = random.randint(1, order - 1)
    public_key = elliptic_multiply(base_point, private_key, a_coeff, modulus)
    return private_key, public_key

def encrypt_point(message_point, public_key, base_point, a_coeff, modulus):
    order = calculate_order(base_point, a_coeff, modulus)
    k = random.randint(1, order - 1)
    ephemeral_key = elliptic_multiply(base_point, k, a_coeff, modulus)
    shared_secret = elliptic_multiply(public_key, k, a_coeff, modulus)
    encrypted_point = elliptic_addition(message_point, shared_secret, a_coeff, modulus)
    return ephemeral_key, encrypted_point

def decrypt_point(cipher1, cipher2, private_key, a_coeff, modulus):
    shared_secret = elliptic_multiply(cipher1, private_key, a_coeff, modulus)
    inverse_shared_secret = (shared_secret[0], (-shared_secret[1]) % modulus)
    plaintext = elliptic_addition(cipher2, inverse_shared_secret, a_coeff, modulus)
    return plaintext

curve_a = 1
curve_b = 1
prime_mod = 23
generator_point = (17, 20)

private_key, public_key = generate_keys(generator_point, curve_a, prime_mod)
print("Private Key:", private_key)
print("Public Key:", public_key)

message_point = (9, 7)

cipher_pair = encrypt_point(message_point, public_key, generator_point, curve_a, prime_mod)
print("Encrypted Message:", cipher_pair)

decrypted_point = decrypt_point(cipher_pair[0], cipher_pair[1], private_key, curve_a, prime_mod)
print("Decrypted Message:", decrypted_point)

if decrypted_point == message_point:
    print("Decryption successful: The decrypted message matches the original.")
else:
    print("Decryption failed: The decrypted message does not match the original.")
