def encrypt_caesar(plaintext: str, offset: int):
    result = ""
    for i in plaintext:
        if i.isalpha():
            if i.islower():
                result += chr((ord(i) - ord('a') + offset) % 26 + ord('a'))
            else:
                result += chr((ord(i) - ord('A') + offset) % 26 + ord('A'))
        else:
            result += i
    return result


def decrypt_caesar(ciphertext: str, offset: int):
    return encrypt_caesar(ciphertext, -offset)


print(encrypt_caesar("hElLo WoRlD", 3))  # kHoOr ZrUoG
print(decrypt_caesar("kHoOr ZrUoG", 3))  # hElLo WoRlD
