from binascii import hexlify, unhexlify


def my_function(text, key):
    if len(text) == len(key):
        unhexly_text, unhexly_key = unhexlify(text), unhexlify(key)
        xored_bytes = bytes([b1 ^ b2 for b1, b2 in zip(unhexly_text, unhexly_key)])
        print(xored_bytes)
        print(hexlify(xored_bytes).decode('ascii'))
    else:
        print('Текст и ключ не совпадают по количеству символов.')

my_function("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965")
