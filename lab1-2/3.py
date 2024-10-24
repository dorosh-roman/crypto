import random

substitution_table = {
    'А': [17, 31, 48],
    'Б': [23, 44, 63],
    'В': [14, 89, 42],
    'Г': [55, 52, 11],
    'Д': [37, 88, 25],
    'Е': [97, 51, 15],
    'Ж': [47, 67, 33],
    'З': [76, 19, 59],
    'И': [27, 64, 73],
    'К': [77, 38, 45]
}

def encrypt(input_text):
    result = []
    for char in input_text.upper():
        if char in substitution_table:
            result.append(str(random.choice(substitution_table[char])))
        else:
            result.append(char)
    return ''.join(result)

def decrypt(cipher_text):
    reverse_table = {str(num): key for key, nums in substitution_table.items() for num in nums}
    result = []
    i = 0
    while i < len(cipher_text):
        if i + 1 < len(cipher_text):
            segment = cipher_text[i:i+2]
            if segment in reverse_table:
                result.append(reverse_table[segment])
                i += 2
                continue
        result.append(cipher_text[i])
        i += 1
    return ''.join(result)

original_text = "ЖАДАЖА"
print(f"Original text: {original_text}")

encrypted_text = encrypt(original_text)
print(f"Encrypted text: {encrypted_text}")

decrypted_text = decrypt(encrypted_text)
print(f"Decrypted text: {decrypted_text}")
