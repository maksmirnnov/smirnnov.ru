def is_ecb(ciphertext):
    blocks = []

    for i in range(len(ciphertext) // 16):
        start = i * 16
        end = (i + 1) * 16
        blocks.append(ciphertext[start:end])

    for i in range(len(blocks)):
        for j in range(len(blocks)):
            if i != j and blocks[i] == blocks[j]:
                return True
    
    return False

if __name__ == "__main__":
    with open('2.txt', 'r') as f:
        for ciphertext in f:
            ciphertext = ciphertext.strip()
            if is_ecb(bytearray.fromhex(ciphertext)):
                print(ciphertext)