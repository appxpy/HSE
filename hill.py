import numpy as np
from typing import Callable
import sys

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def validate_middleware(message: str, key: str, function: Callable):
    keys = key.split(',')
    if any([int(len(k) ** .5) % 1 for k in keys]):
        print('Error: Key must have a square shape matrix.')
        sys.exit(1)
    return function(message, key)


def get_inverse_key(key):
    return np.mod(np.array(np.linalg.inv(key), dtype=np.float32), len(alphabet))


def hill_encrypt(message: str, key: str):
    K = np.array([alphabet.index(i) for i in key.upper()]).reshape(int(len(key) ** 0.5), int(len(key) ** 0.5))
    BLOCK_SIZE = K.shape[0]
    message = message + 'A' * (BLOCK_SIZE - (len(message) % BLOCK_SIZE)) if len(message) % BLOCK_SIZE != 0 else message
    CHUNKS = [np.array([alphabet.index(i) for i in message[i:i + BLOCK_SIZE].upper()]).reshape(K.shape[0], -1) for i in range(0, len(message), BLOCK_SIZE)]
    C = ''
    for chunk in CHUNKS:
        C += ''.join([alphabet[i] for i in (np.dot(K, chunk) % len(alphabet)).flatten()])
    return C


def hill_decrypt(ciphertext: str, key: str):
    K = np.array([alphabet.index(i) for i in key.upper()]).reshape(int(len(key) ** 0.5), int(len(key) ** 0.5))
    K_INV = get_inverse_key(K)
    BLOCK_SIZE = K.shape[0]
    message = ciphertext + 'A' * (BLOCK_SIZE - (len(ciphertext) % BLOCK_SIZE)) if len(ciphertext) % BLOCK_SIZE != 0 else ciphertext
    CHUNKS = [np.array([alphabet.index(i) for i in message[i:i + BLOCK_SIZE].upper()]).reshape(K.shape[0], -1) for i in range(0, len(message), BLOCK_SIZE)]
    P = ''
    for chunk in CHUNKS:
        P += ''.join([alphabet[int(i)] for i in (np.dot(K_INV, chunk) % len(alphabet)).flatten()])
    return P


def recurrent_hill_encrypt(message: str, key: str):
    KEYS = [np.array([alphabet.index(i) for i in k.upper()]).reshape(int(len(k) ** 0.5), int(len(k) ** 0.5)) for k in key.split(',')]
    if len(KEYS) != 2:
        print('Error: For recurrent algorythm you must specify exactly 2 keys!')
        sys.exit(1)
    BLOCK_SIZE = KEYS[0].shape[0]
    message = message + 'A' * (BLOCK_SIZE - (len(message) % BLOCK_SIZE)) if len(message) % BLOCK_SIZE != 0 else message
    CHUNKS = [np.array([alphabet.index(i) for i in message[i:i + BLOCK_SIZE].upper()]).reshape(KEYS[0].shape[0], -1) for i in range(0, len(message), BLOCK_SIZE)]
    C = ''
    for iter_index in range(len(CHUNKS)):
        if iter_index > 1:
            KEYS.append(np.mod(np.dot(KEYS[-1], KEYS[-2]), 26))
        encrypted = np.dot(KEYS[iter_index], CHUNKS[iter_index]) % 26
        C += ''.join([alphabet[i] for i in encrypted.flatten()])
    return C


def recurrent_hill_decrypt(ciphertext: str, key: str):
    KEYS = [np.array([alphabet.index(i) for i in k.upper()], dtype=np.float32).reshape(int(len(k) ** 0.5), int(len(k) ** 0.5)) for k in key.split(',')]
    if len(KEYS) != 2:
        print('Error: For recurrent algorythm you must specify exactly 2 keys!')
        sys.exit(1)
    try:
        INV_KEYS = [get_inverse_key(i) for i in KEYS]
        print(INV_KEYS)
    except Exception:
        print('Error: Key matrix must be invertible!')
        sys.exit(1)
    BLOCK_SIZE = INV_KEYS[0].shape[0]
    ciphertext = ciphertext + 'A' * (BLOCK_SIZE - (len(ciphertext) % BLOCK_SIZE)) if len(ciphertext) % BLOCK_SIZE != 0 else ciphertext
    CHUNKS = [np.array([alphabet.index(i) for i in ciphertext[i:i + BLOCK_SIZE].upper()]).reshape(KEYS[0].shape[0], -1) for i in range(0, len(ciphertext), BLOCK_SIZE)]
    P = ''
    for iter_index in range(len(CHUNKS)):
        if iter_index > 1:
            INV_KEYS.append(np.dot(INV_KEYS[-2], INV_KEYS[-1]) % 26)
        decrypted = np.dot(INV_KEYS[iter_index], CHUNKS[iter_index]) % 26
        P += ''.join([alphabet[int(i)] for i in decrypted.flatten()])
    return P


def main(silent):
    if not silent['enabled']:
        print('Supported algorythms:')
        print('- 1. DH/dh - Default Hill Algorythm')
        print('- 2. RH/dh - Recurrent Hill Algorithm')
        print()
        print('Mode selection:')
        print('- E/e - Encrypt')
        print('- D/d - Decrypt')
        print()
        print()
        alg = input('Please, select algorythm (DH/RH/dh/rh): ')
        print()
        if alg not in ['DH', 'RH', 'dh', 'rh']:
            print('Error: Invalid algorythm selected.')
            sys.exit(1)
        mode = input('Please, select mode (E/e/D/d): ')
        print()
        if mode not in ['E', 'e', 'D', 'd']:
            print('Error: Invalid mode selected.')
            sys.exit(1)
        payload = input('Please enter message/ciphertext: ').upper()
        print()
        print('**Note: if you\'re using RH alhorythm, separate two keys by comma. Example: HELLO,WORLD **')
        key = input('Please enter key (in string format): ').upper()
        if alg.lower() == 'dh':
            fn = (hill_encrypt, hill_decrypt)
        else:
            fn = (recurrent_hill_encrypt, recurrent_hill_decrypt)
        if mode.lower() == 'e':
            print(f'message: {payload}, key: {key} -> {fn[0].__name__} -> {validate_middleware(payload, key, fn[0])}')
        else:
            print(f'ciphertext: {payload}, key: {key} -> {fn[1].__name__} -> {validate_middleware(payload, key, fn[1])}')
    else:
        if silent['algorythm'].lower() == 'dh':
            fn = (hill_encrypt, hill_decrypt)
        else:
            fn = (recurrent_hill_encrypt, recurrent_hill_decrypt)
        payload = silent['payload'].upper()
        key = silent['key'].upper()
        if silent['mode'].lower() == 'e':
            print(f'message: {payload}, key: {key} -> {fn[0].__name__} -> {validate_middleware(payload, key, fn[0])}')
        else:
            print(f'ciphertext: {payload}, key: {key} -> {fn[1].__name__} -> {validate_middleware(payload, key, fn[1])}')


if __name__ == "__main__":
    # Pre-defined variables to avoid spending time on manual input
    NOINPUT = {
        'enabled': True,  # Leave this false to enable input
        'algorythm': 'rh',
        'mode': 'E',
        'payload': 'GEORGE',
        'key': 'fchd,fccb'
    }
    main(NOINPUT)
