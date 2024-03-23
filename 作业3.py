def caesar_cipher(n, plaintext):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - shift + n) % 26 + shift)
            ciphertext += encrypted_char
        else:
            ciphertext += char
    return ciphertext

# 获取输入参数
try:
    n, plaintext = input().split(maxsplit=1)
    n = int(n)
except ValueError:
    print("illegal input")
else:
    # 调用加密函数并输出结果
    result = caesar_cipher(n, plaintext)
    print(result)
