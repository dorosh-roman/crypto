def gf_multiply(byte1, byte2):
    if isinstance(byte1, str):
        byte1 = int(byte1, 16)
    if isinstance(byte2, str):
        byte2 = int(byte2, 16)
    
    result = 0
    for _ in range(8):
        if byte2 & 1:
            result ^= byte1
        
        carry = byte1 & 0x80
        byte1 = (byte1 << 1) & 0xFF
        if carry:
            byte1 ^= 0x1B
        
        byte2 >>= 1
    
    return result

byte1 = 0x57
byte2 = 0x83

result = gf_multiply(byte1, byte2)

print(f"{hex(byte1)} * {hex(byte2)} = {hex(result)}")
