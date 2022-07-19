import requests
import binascii


if __name__ == "__main__":
    sig = bytearray("\x00" * 20, 'utf8')

    for i in range(20):
        response_times = []
        for b in range(256):
            sig[i] = b
            url = "http://localhost:8080/?file=secret.txt&signature={0}".format(binascii.hexlify(sig))
            r = requests.get(url)
            response_times.append(r.elapsed.total_seconds())
        sig[i] = response_times.index(max(response_times))
        print(binascii.hexlify(sig))
    print(binascii.hexlify(sig))
