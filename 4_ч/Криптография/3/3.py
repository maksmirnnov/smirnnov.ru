import bcrypt
from multiprocessing import Pool


SALT = '$2b$04$l7a9porj89C.Afh4n8orYu'

def crypt(password):
    return bcrypt.hashpw(password, SALT)

if __name__ == "__main__":
    with open('rockyou.txt', 'r') as f:
        rockyou = f.read().splitlines()
    
    p = Pool(3)

    digests = p.map(crypt, rockyou)
    
    with open('bcrypt_rockyou.txt', 'w') as f:
        f.write('\n'.join(digests))
