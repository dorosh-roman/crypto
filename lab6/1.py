def mul02(byte):
    if isinstance(byte, str):
        byte = int(byte, 16)
    
    if byte & 0x80:
        result = (byte << 1) ^ 0x1B
    else:
        result = byte << 1
    
    return result & 0xFF


def mul03(byte):
    return mul02(byte) ^ byte


byte_D4 = 0xD4  
byte_BF = 0xBF  

result_D4_mul02 = mul02(byte_D4)
result_BF_mul03 = mul03(byte_BF)

print(f"{hex(byte_D4)} * 02 = {hex(result_D4_mul02)}")
print(f"{hex(byte_BF)} * 03 = {hex(result_BF_mul03)}")