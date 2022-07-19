#! Python2
from Crypto.Cipher import AES
import base64


def xor(block1, block2):
    if len(block1) == len(block2):
        return "".join(map(lambda a, b: chr(a ^ ord(b)), block1, block2))


def aes128_encrypt(block, key):
    if len(block) != 16:
        return None
    cipher = AES.new(key, AES.MODE_ECB)
    return bytearray(cipher.encrypt(block))


def aes128_decrypt(block, key):
    if len(block) != 16:
        return None
    cipher = AES.new(key, AES.MODE_ECB)
    return bytearray(cipher.decrypt(block))


def aes128_cbc_encrypt(iv, plaintext, key):
    ciphertext = iv
    ciphertext_block = iv
    for i in range(len(plaintext) // 16):
        start = i * 16
        end = (i + 1) * 16
        plaintext_block = plaintext[start:end]
        plaintext_block = xor(plaintext_block, ciphertext_block)
        ciphertext_block = aes128_encrypt(plaintext_block, key)
        ciphertext += ciphertext_block
    return ciphertext


def aes128_cbc_decrypt(ciphertext, key):
    plaintext = bytearray()
    iv = ciphertext[:16]
    prev_ciphertext_block = iv
    for i in range(1, len(ciphertext) // 16):
        start = i * 16
        end = (i + 1) * 16
        ciphertext_block = ciphertext[start:end]
        decrypted_block = aes128_decrypt(ciphertext_block, key)
        plaintext_block = xor(decrypted_block, prev_ciphertext_block)
        prev_ciphertext_block = ciphertext_block
        plaintext += plaintext_block
    return plaintext


if __name__ == '__main__':
    iv = bytearray('\x00' * 16)
    key = 'YELLOW SUBMARINE'

    with open('4.txt', 'r') as f:
        ciphertext_b64 = ''.join(f.read().splitlines())

    ciphertext = base64.b64decode(ciphertext_b64)
    plaintext = aes128_cbc_decrypt(ciphertext, key)
    print(plaintext)
