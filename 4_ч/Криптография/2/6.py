#! Python2
import os
from Crypto.Cipher import AES
import base64


KEY = os.urandom(16)
UNKNOWN_STRING = base64.b64decode('Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK')


def aes128_encrypt(block, key):
    if len(block) != 16:
        return None
    cipher = AES.new(key, AES.MODE_ECB)
    return bytearray(cipher.encrypt(block))


def aes128_ecb_encrypt(plaintext, key):
    ciphertext = bytearray()

    for i in range(len(plaintext) // 16):
        start = i * 16
        end = (i + 1) * 16
        ciphertext_block = aes128_encrypt(plaintext[start:end], key)
        ciphertext += ciphertext_block
    
    return plaintext


def ecb_cbc_detection_oracle(ciphertext):
    for i in range(len(ciphertext) - 16):
        if ciphertext[i:i+16] == ciphertext[i+16:i+32]:
            return "ECB"
    return "CBC"


def encrypt(plaintext):
    return aes128_ecb_encrypt(plaintext + UNKNOWN_STRING, KEY)


def crack_block_size():
    tmp = 0
    for i in range(1, 33):
        payload = i * "A"
        ciphertext = encrypt(bytearray(payload))
        if len(ciphertext) != tmp and tmp != 0:
            return len(ciphertext) - tmp
        tmp = len(ciphertext)
    return 0


def crack_byte(plaintext, known_string):
    block_x = encrypt(bytearray(plaintext))
    for i in range(256):
        tmp = encrypt(bytearray(plaintext + known_string + chr(i)))
        l = len(plaintext) + len(known_string) + 1
        if tmp[:l] == block_x[:l]:
            return bytearray([i])
    return None


def crack():
    unknown_string = bytearray()
    unknown_string_length = len(encrypt(bytearray()))
    for i in range(1, unknown_string_length):
        payload = bytearray("A" * (unknown_string_length - i))
        byte = crack_byte(payload, unknown_string)
        if not byte:
            break
        unknown_string += byte
    return unknown_string

print(crack())
