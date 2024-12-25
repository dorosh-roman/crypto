def left_rotate(val, shift):
    return ((val << shift) | (val >> (32 - shift))) & 0xFFFFFFFF

def pack_words_as_bytes(words):
    return b''.join(word.to_bytes(4, byteorder='big') for word in words)

def compute_sha1(message):
    original_length = len(message)
    message += b'\x80'
    padding = (56 - (original_length + 1) % 64) % 64
    message += b'\x00' * padding
    message += (original_length * 8).to_bytes(8, byteorder='big')

    h_values = [
        0x67452301,
        0xEFCDAB89,
        0x98BADCFE,
        0x10325476,
        0xC3D2E1F0
    ]

    for chunk_start in range(0, len(message), 64):
        chunk = message[chunk_start:chunk_start + 64]
        w = [int.from_bytes(chunk[i:i + 4], byteorder='big') for i in range(0, 64, 4)]
        for i in range(16, 80):
            w.append(left_rotate(w[i - 3] ^ w[i - 8] ^ w[i - 14] ^ w[i - 16], 1))

        a, b, c, d, e = h_values

        for i in range(80):
            if i < 20:
                f, k = (b & c) | (~b & d), 0x5A827999
            elif i < 40:
                f, k = b ^ c ^ d, 0x6ED9EBA1
            elif i < 60:
                f, k = (b & c) | (b & d) | (c & d), 0x8F1BBCDC
            else:
                f, k = b ^ c ^ d, 0xCA62C1D6

            temp = (left_rotate(a, 5) + f + e + k + w[i]) & 0xFFFFFFFF
            e, d, c, b, a = d, c, left_rotate(b, 30), a, temp

        h_values = [
            (h_values[0] + a) & 0xFFFFFFFF,
            (h_values[1] + b) & 0xFFFFFFFF,
            (h_values[2] + c) & 0xFFFFFFFF,
            (h_values[3] + d) & 0xFFFFFFFF,
            (h_values[4] + e) & 0xFFFFFFFF
        ]

    return pack_words_as_bytes(h_values)

user_text = input("Enter the text to hash: ").encode("UTF-8")
hash_output = compute_sha1(user_text).hex()
print(f'Message hash: {hash_output}')