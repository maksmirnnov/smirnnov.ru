import bcrypt
import hashlib


with open('1.txt', 'r') as file:
    passwords = file.read().splitlines()


def get_bcrypted_hash():
    for password in passwords:
        hashed = bcrypt.hashpw(bytes(password, 'utf8'), bytes('$2b$15$NSVH/I.9u1l/WoYUd/sSI.', 'utf8'))
        if bcrypt.checkpw(bytes(password, 'utf8'), hashed):
            print(hashed)
# get_bcrypted_hash()


def get_md5_hash():
    for password in passwords:
        print(hashlib.md5(bytes(password, 'utf8')).hexdigest())
# get_md5_hash()


def get_sha256_hash():
    for password in passwords:
        print(hashlib.sha256(bytes(password, 'utf8')).hexdigest())
# get_sha256_hash()
