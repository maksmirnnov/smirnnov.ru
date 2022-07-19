import sys
import sha1

def mac(message):
    KEY = "TEST"
    return sha1.sha1(KEY + message)

if __name__ == "__main__":
    message = sys.argv[1]
    print(message, mac(message))
