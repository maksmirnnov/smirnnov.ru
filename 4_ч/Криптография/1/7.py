open_text1 = bytearray(b"Burning 'em, if you ain't quick and nimble")
open_text2 = bytearray(b"I go crazy when I hear a cymbal")
key = bytearray(b"ICE")


def encode(plain_text, key):
    i = 0
    cipher_text = bytearray()

    for char in plain_text:
        cipher_text.append(char ^ key[i % 3])
        i += 1
    
    print(bytearray.hex(cipher_text))

encode(open_text1, key)
encode(open_text2, key)
