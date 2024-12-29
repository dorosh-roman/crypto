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

def elliptic_point_addition(p1, p2, a, modulus):
    if p1 == (None, None):
        return p2
    if p2 == (None, None):
        return p1
    if p1[0] == p2[0] and p1[1] != p2[1]:
        return (None, None)

    if p1 == p2:
        inv = modular_inverse(2 * p1[1], modulus)
        slope = (3 * pow(p1[0], 2, modulus) + a) * inv % modulus
    else:
        inv = modular_inverse(p2[0] - p1[0], modulus)
        slope = (p2[1] - p1[1]) * inv % modulus

    x3 = (pow(slope, 2, modulus) - p1[0] - p2[0]) % modulus
    y3 = (slope * (p1[0] - x3) - p1[1]) % modulus
    return x3, y3

def point_scalar_multiplication(point, scalar, a, modulus):
    result = (None, None)
    temp_point = point

    for bit in bin(scalar)[2:]:
        if bit == '1':
            result = elliptic_point_addition(result, temp_point, a, modulus)
        temp_point = elliptic_point_addition(temp_point, temp_point, a, modulus)

    return result

def find_point_order(point, a, modulus):
    count = 1
    temp = point
    print(f"Point {count}: {temp}")
    while temp != (None, None):
        temp = elliptic_point_addition(temp, point, a, modulus)
        count += 1
        print(f"Point {count}: {temp}")
    return count

# Elliptic curve parameters
curve_a = 1
curve_b = 1
modulus = 23
sample_point = (17, 20)

# Verify if the point lies on the curve
if pow(sample_point[1], 2, modulus) == (pow(sample_point[0], 3, modulus) + curve_a * sample_point[0] + curve_b) % modulus:
    order = find_point_order(sample_point, curve_a, modulus)
    print(f"Order of point {sample_point} on the curve y^2 ≡ x^3 + {curve_a}x + {curve_b} (mod {modulus}): {order}")
else:
    print("The given point does not lie on the elliptic curve!")
