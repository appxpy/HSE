def encrypt_affine(plaintext: str, multiplier: int, offset: int):
    result = ""
    for i in plaintext:
        if i.isalpha():
            if i.islower():
                charMod = (ord(i) - ord('a')) * multiplier + offset
                result += chr(charMod % 26 + ord('a'))
            else:
                charMod = (ord(i) - ord('A')) * multiplier + offset
                result += chr(charMod % 26 + ord('A'))
        else:
            result += i
    return result


def decrypt_affine(ciphertext: str, multiplier: int, offset: int):
    result = ""
    multiplier_inverse = 0
    for k in range(26):
        if (multiplier * k) % 26 == 1:
            multiplier_inverse = k
            break
    for i in ciphertext:
        if i.isalpha():
            if i.islower():
                charMod = ((ord(i) - ord('a')) - offset) * (multiplier_inverse)
                result += chr(charMod % 26 + ord('a'))
            else:
                charMod = ((ord(i) - ord('A')) - offset) * (multiplier_inverse)
                result += chr(charMod % 26 + ord('A'))
        else:
            result += i
    return result


print(encrypt_affine("HELLO", 7, 5))  # CHEEZ
print(decrypt_affine("CHEEZ", 7, 5))  # HELLO
