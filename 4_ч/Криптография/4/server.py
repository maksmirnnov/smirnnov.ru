import web
import hmac
import time
import binascii


def insecure_compare(s1, s2):
    b1 = bytearray(binascii.unhexlify(s1))
    b2 = bytearray(binascii.unhexlify(s2))

    for i in range(len(min(b1, b2))):
        if b1[i] != b2[i]:
            return False
        time.sleep(0.05)
    return True

KEY = 'YELLOW SUBMARINE'
urls = (
    '/', 'hello'
)
app = web.application(urls, globals())

class hello:
    def GET(self):
        params = web.input(_method='get')
        fil = params['file'] if 'file' in params else None
        signature = params['signature'] if 'signature' in params else None

        if fil and signature and len(signature) == 40:
            with open(fil, 'r') as f:
                file_content = f.read()
            file_hmac = hmac.hmac(bytearray(file_content), bytearray(KEY))
            if insecure_compare(file_hmac, signature):
                return file_content
        return "Access Denied..."

if __name__ == "__main__":
    app.run()