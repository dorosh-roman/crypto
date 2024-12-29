def find_elliptic_curve_points(coeff_a, coeff_b, modulus):
    curve_points = []
    for x in range(modulus):
        y_squared = (pow(x, 3, modulus) + coeff_a * x + coeff_b) % modulus  
        for y in range(modulus):
            if pow(y, 2, modulus) == y_squared:  
                curve_points.append((x, y))
    return curve_points

param_a = 1
param_b = 1
modulo_p = 23

curve_points = find_elliptic_curve_points(param_a, param_b, modulo_p)

print("Points on the elliptic curve for the equation y^2 ≡ x^3 + x + 1 (mod 23):")
print(", ".join(map(str, curve_points)))
