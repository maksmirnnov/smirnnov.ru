#! Python2
import os
from Crypto.Cipher import AES


def random_bytearray(length_min, length_max):
    num_of_bytes = ord(os.urandom(1)) % (length_max - length_min) + length_min
    return bytearray(os.urandom(num_of_bytes))

def random_key():
    return bytearray(os.urandom(16))

def random_bool():
    return ord(os.urandom(1)) & 1

def pkcs7_padding(block, target_length):
    block_padded = block

    if len(block) % target_length == 0:
        pad_length = target_length
    else:
        pad_length = target_length - (len(block) % target_length)
    
    pad_byte = pad_length

    for i in range(pad_length):
        block_padded.append(pad_byte)
    
    return block_padded

def xor(block1, block2):
    if len(block1) == len(block2):
        return "".join(map(lambda a, b: chr(a ^ b), block1, block2))


def aes128_ecb_encrypt(block, key):
    if len(block) != 16:
        return None
    cipher = AES.new(key, AES.MODE_ECB)
    return bytearray(cipher.encrypt(block))


def aes128_cbc_encrypt(iv, plaintext, key):
    ciphertext = iv
    ciphertext_block = iv
    for i in range(len(plaintext) // 16):
        start = i * 16
        end = (i + 1) * 16
        plaintext_block = plaintext[start:end]
        plaintext_block = xor(plaintext_block, ciphertext_block)
        ciphertext_block = aes128_ecb_encrypt(plaintext_block, key)
        ciphertext += ciphertext_block
    return ciphertext


def encryption_oracle(plaintext):
    hard = random_bytearray(5, 10)
    tail = random_bytearray(5, 10)
    plaintext = hard + plaintext + tail
    plaintext = pkcs7_padding(plaintext, 16)

    key = random_key()
    ciphertext = bytearray()

    if random_bool():
        print('Actual mode is ECB')
        ciphertext = aes128_ecb_encrypt(plaintext, key)
    else:
        print('Actual mode is CBC')
        iv = random_key()
        ciphertext = aes128_cbc_encrypt(iv, plaintext, key)
    return ciphertext

def ecb_cbc_detection_oracle(ciphertext):
    for i in range(16, len(ciphertext) - 16):
        if ciphertext[i:i+16] == ciphertext[i+16:i+32]:
            return "ECB"
    return "CBC"


ciphertext = encryption_oracle('YELLOW SUBMARINEYELLOW SUBMARINEYELLOW SUBMARINEYELLOW SUBMARINE')
print('Detected {0}'.format(ecb_cbc_detection_oracle(ciphertext)))