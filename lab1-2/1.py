def clean_text(text):
    cleaned_text = ""
    for char in text:
        if char.isalnum():
            cleaned_text += char
    return cleaned_text

def create_matrix(text, rows, cols):
    matrix = []
    cleaned_text = clean_text(text)
    
    index = 0
    for _ in range(rows):
        row = []
        for _ in range(cols):
            if index < len(cleaned_text):
                row.append(cleaned_text[index])
                index += 1
            else:
                row.append(' ')  
        matrix.append(row)
    
    return matrix

def get_sorted_indices(key):
    key_with_indices = []
    for idx in range(len(key)):
        key_with_indices.append((key[idx], idx))

    key_with_indices.sort()

    sorted_indices = []
    for pair in key_with_indices:
        char, idx = pair
        sorted_indices.append(idx)

    return sorted_indices

def encrypt_message(text, row_key, col_key):
    num_rows = len(row_key)
    num_cols = len(col_key)

    matrix = create_matrix(text, num_rows, num_cols)

    sorted_col_indices = get_sorted_indices(col_key)
    sorted_row_indices = get_sorted_indices(row_key)

    encrypted_message = ""
    for col in sorted_col_indices:
        for row in sorted_row_indices:
            encrypted_message += matrix[row][col]

    return encrypted_message

def get_space_positions(text):
    space_positions = []
    for i in range(len(text)):
        if text[i] == ' ':
            space_positions.append(i)
    return space_positions

def decrypt_message(encrypted_text, row_key, col_key, space_positions):
    num_rows = len(row_key)
    num_cols = len(col_key)

    matrix = []
    for _ in range(num_rows):
        row = []
        for _ in range(num_cols):
            row.append(' ')  
        matrix.append(row)

    sorted_col_indices = get_sorted_indices(col_key)
    sorted_row_indices = get_sorted_indices(row_key)

    index = 0
    for col in sorted_col_indices:
        for row in sorted_row_indices:
            if index < len(encrypted_text):
                matrix[row][col] = encrypted_text[index]
                index += 1

    decrypted_message = ""
    for row in range(num_rows):
        for col in range(num_cols):
            decrypted_message += matrix[row][col]

    decrypted_message_list = []
    for char in decrypted_message.strip():
        decrypted_message_list.append(char)

    for pos in space_positions:
        if pos < len(decrypted_message_list):
            decrypted_message_list.insert(pos, ' ')

    return ''.join(decrypted_message_list).strip()

if __name__ == "__main__":
    original_text = "тестовий рядок символів"
    column_key = "крипто"
    row_key = "шифр"

    print(f"Original text: {original_text}")

    space_positions = get_space_positions(original_text)

    encrypted_text = encrypt_message(original_text, row_key, column_key)
    print(f"Encrypted text: {encrypted_text}")

    decrypted_text = decrypt_message(encrypted_text, row_key, column_key, space_positions)
    print(f"Decrypted text: {decrypted_text}")