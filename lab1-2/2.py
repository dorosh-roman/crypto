def gronsfeld_table():
    """Creates the Gronsfeld cipher alphabet table."""
    table = {
        0: "АБВГДЕЖЗИК",
        1: "КАБВГДЕЖЗИ",
        2: "ИКАБВГДЕЖЗ",
        3: "ЗИКАБВГДЕЖ",
        4: "ЖЗИКАБВГДЕ",
        5: "ЕЖЗИКАБВГД",
        6: "ДЕЖЗИКАБВГ"
    }
    return table

def encrypt_gronsfeld_custom(plaintext, key):
    """Encrypts text using the Gronsfeld cipher and a numeric key."""
    table = gronsfeld_table()
    ciphertext = []
    
    key_numbers = []
    for char in key:
        key_numbers.append(int(char))

    for i in range(len(plaintext)):
        current_char = plaintext[i].upper()
        
        if current_char in table[0]:
            char_index = table[0].index(current_char)
            current_row = table[key_numbers[i % len(key_numbers)]]
            ciphertext.append(current_row[char_index])
        else:
            ciphertext.append(current_char)  

    return ''.join(ciphertext)

def decrypt_gronsfeld_custom(ciphertext, key):
    """Decrypts text using the Gronsfeld cipher and a numeric key."""
    table = gronsfeld_table()
    plaintext = []
    
    key_numbers = []
    for char in key:
        key_numbers.append(int(char))

    for i in range(len(ciphertext)):
        current_char = ciphertext[i].upper()
        
        if current_char in table[0]:
            current_row = table[key_numbers[i % len(key_numbers)]]
            char_index = current_row.index(current_char)
            plaintext.append(table[0][char_index])
        else:
            plaintext.append(current_char)  

    return ''.join(plaintext)

plaintext = "ЗАДВИЖКА"
key = "513"
encrypted = encrypt_gronsfeld_custom(plaintext, key)
print(f"Encrypted text: {encrypted}")

decrypted = decrypt_gronsfeld_custom(encrypted, key)
print(f"Decrypted text: {decrypted}")
