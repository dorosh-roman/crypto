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
            j += 1
        if u != n - 1:
            return False
    return True


def generate_large_prime(bits=1024):
    found = False
    while not found:
        num = random.getrandbits(bits) | (1 << (bits - 1)) | 1
        if miller_rabin(num, 25):
            found = True
    return num


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
    return a, x0, y0


def generate_keys(bits=1024):
    prime1 = generate_large_prime(bits)
    prime2 = generate_large_prime(bits)

    while prime1 == prime2:
        prime2 = generate_large_prime(bits)

    modulus = prime1 * prime2
    totient = (prime1 - 1) * (prime2 - 1)

    public_exponent = 65537
    if gcdex(public_exponent, totient)[0] != 1:
        raise ValueError("Public exponent and totient are not coprime")

    private_exponent = gcdex(public_exponent, totient)[1] % totient

    return (public_exponent, modulus), (private_exponent, modulus)



def encrypt(message, pub_key):
    exp, mod = pub_key
    encrypted = pow(message, exp, mod)
    return encrypted

def decrypt(encoded, priv_key):
    exp, mod = priv_key
    decrypted = pow(encoded, exp, mod)
    return decrypted


public_key, private_key = generate_keys()

message = 100  
ciphertext = encrypt(message, public_key)
decrypted_message = decrypt(ciphertext, private_key)

print("Original message -", message)
print("Encrypted message -", ciphertext)
print("Decrypted message -", decrypted_message)