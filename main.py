#!/usr/bin/env python3

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

group_number = 15
encrypted_file = "input-files/encrypted" + str(group_number) + ".txt"
word_file = "input-files/wordsEn.txt"

def pad_str(input):
    length = len(input)
    to_pad_to = 16

    if length < to_pad_to:
        # append thing
        for _ in range(length, to_pad_to + 1):
            input += ' '
    elif length > to_pad_to:
        input = input[0:to_pad_to + 1]

    return input

file = open(word_file, 'r')
iv_str = '0' * 16
iv = bytes(iv_str, 'ascii')

for word in file:
    key = bytes(pad_str(word), 'ascii')
    decryptor = Cipher(
        algorithms.AES128(key),
        modes.CBC(iv)
    )
