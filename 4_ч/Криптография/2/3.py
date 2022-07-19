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
if __name__ == "__main__":
    m1 = bytearray("YELLOW SUBMARINE".encode('utf8'))
    m2 = bytearray("YELLOW SUBMARINE YELLOW SUBMARINE".encode('utf8'))
    m3 = bytearray("YELLOW SUBMARINE".encode('utf8'))

    print(pkcs7_padding(m1, 16))
    print(pkcs7_padding(m2, 16))
    print(pkcs7_padding(m3, 20))
