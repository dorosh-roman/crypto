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

def generate_prime_number(bit_length):
    while True:
        candidate = random.getrandbits(bit_length) | 1  
        if miller_rabin(candidate, 5):  
            return candidate

def find_primitive_root(modulo):
    phi = modulo - 1
    while True:
        candidate = random.randint(2, modulo - 1)
        if pow(candidate, 2, modulo) != 1 and pow(candidate, phi // 2, modulo) != 1:
            return candidate

def encode_text(text):
    return [ord(char) for char in text]

def decode_text(encoded):
    return ''.join(chr(num) for num in encoded)

def generate_keys(bits):
    p = generate_prime_number(bits)
    g = find_primitive_root(p)
    x = random.randint(1, p - 2)
    y = pow(g, x, p)
    return (p, g, y), (p, x)

def encrypt_message(message, p, g, y):
    encoded_message = encode_text(message)
    k = random.randint(1, p - 2)
    c1 = pow(g, k, p)
    c2 = [(char * pow(y, k, p)) % p for char in encoded_message]
    return c1, c2

def decrypt_message(ciphertext, p, x):
    c1, c2 = ciphertext
    shared_secret = pow(c1, x, p)
    shared_secret_inv = pow(shared_secret, -1, p)
    decoded_message = [(char * shared_secret_inv) % p for char in c2]
    return decode_text(decoded_message)

(public_key, private_key) = generate_keys(256)
p, g, y = public_key
_, x = private_key

input_message = input("Enter a message: ")

encrypted_message = encrypt_message(input_message, p, g, y)
decrypted_message = decrypt_message(encrypted_message, p, x)

print(f"Encrypted: {encrypted_message}")
print(f"Decrypted: {decrypted_message}")
