def encrypt_affine_recursive(plaintext: str, multiplier: int, offset: int):
    if plaintext == "":
        return ""
    else:
        if plaintext[0].isalpha():
            if plaintext[0].islower():
                charMod = (ord(plaintext[0]) - ord('a')) * multiplier + offset
                return chr(charMod % 26 + ord('a')) + encrypt_affine_recursive(plaintext[1:], multiplier, offset)
            else:
                charMod = (ord(plaintext[0]) - ord('A')) * multiplier + offset
                return chr(charMod % 26 + ord('A')) + encrypt_affine_recursive(plaintext[1:], multiplier, offset)
        else:
            return plaintext[0] + encrypt_affine_recursive(plaintext[1:], multiplier, offset)


def decrypt_affine_recursive(ciphertext: str, multiplier: int, offset: int):
    if ciphertext == "":
        return ""
    else:
        multiplier_inverse = 0
        for k in range(26):
            if (multiplier * k) % 26 == 1:
                multiplier_inverse = k
                break
        if ciphertext[0].isalpha():
            if ciphertext[0].islower():
                charMod = ((ord(ciphertext[0]) - ord('a')) - offset) * (multiplier_inverse)
                return chr(charMod % 26 + ord('a')) + decrypt_affine_recursive(ciphertext[1:], multiplier, offset)
            else:
                charMod = ((ord(ciphertext[0]) - ord('A')) - offset) * (multiplier_inverse)
                return chr(charMod % 26 + ord('A')) + decrypt_affine_recursive(ciphertext[1:], multiplier, offset)
        else:
            return ciphertext[0] + decrypt_affine_recursive(ciphertext[1:], multiplier, offset)


print(encrypt_affine_recursive("HELLO", 7, 5))  # CHEEZ
print(decrypt_affine_recursive("CHEEZ", 7, 5))  # HELLO
