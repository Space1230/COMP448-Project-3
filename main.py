#!/usr/bin/env python3

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

encrypted_file = "input-files/encrypted15.txt"
word_file = "input-files/wordsEn.txt"

encrypted_file = open(encrypted_file, 'rb')
encrypted_data = encrypted_file.read()


def pad_str(input):
    input = input.strip()
    length = len(input)
    to_pad_to = 16

    if length < to_pad_to:
        # append thing
        for _ in range(length, to_pad_to):
            input += ' '
    elif length > to_pad_to:
        input = input[0:to_pad_to]

    return input

file = open(word_file, 'r')
iv_str = '0' * 16
iv = bytes(iv_str, 'ascii')

for word in file:
    key = bytes(pad_str(word), 'ascii')

    decryptor = Cipher(
        algorithms.AES128(key),
        modes.CBC(iv)
    ).decryptor()

    plaintext_bytes:bytes = decryptor.update(encrypted_data) + decryptor.finalize()

    try:
        plaintext = plaintext_bytes.decode('ascii').strip()
        if 'the' in plaintext:
            print(plaintext)
            print("key:", key)
    except ValueError:
        continue
