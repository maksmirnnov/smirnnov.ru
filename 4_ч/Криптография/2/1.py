from Crypto.Cipher import AES
import base64


def base64_to_bytes(b64):
    return bytes(base64.b64decode(b64))


def aes128_decrypt(block, key):
    if len(block) != 16:
        return None

    cipher = AES.new(key.encode("utf8"), AES.MODE_ECB)
    return cipher.decrypt(block)


def aes128_ecb_decrypt(ciphertext, key):
    plaintext = bytearray()

    for i in range(len(ciphertext) // 16):
        start = i * 16
        end = (i + 1) * 16
        plaintext_block = aes128_decrypt(ciphertext[start:end], key)
        plaintext += plaintext_block
    
    return plaintext.decode('utf8')


if __name__ == "__main__":
    with open('1.txt', 'r') as f:
        ciphertext = base64_to_bytes("".join(f.read().splitlines()))

    key = "YELLOW SUBMARINE"
    print(aes128_ecb_decrypt(ciphertext, key))
