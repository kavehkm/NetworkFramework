# standard
import os
# internal
import funcs


def menu():
    # first clear screen
    os.system('cls')
    # menu items
    menu = [
        '1) port scanner',
        '2) dns lookup',
        '3) ip locator',
        'x) exit'
    ]
    # get user choice
    return input('\n'.join(menu) + '\n')


while True:
    # show menu and get user answer
    ans = menu()

    # dispatch user answer
    if ans == '1':
        ip = input('ip? ').strip()
        _from = input('from?[1] ').strip()
        _to = input('to?[65535] ').strip()
        # clean input
        _from = int(_from) if _from else 1
        _to = int(_to) if _to else 65535
        # scan ports from _from to _to
        for port in range(_from, _to + 1):
            if funcs.port_scan(ip, port):
                print(port, 'is open')
            else:
                print(port, 'is close')
    elif ans == '2':
        hostname = input('hostname? ').strip()
        ext = input('with extention?[y/n] ').strip()
        ext = True if ext == 'y' else False
        print(funcs.dns_lookup(hostname, ext))
    elif ans == '3':
        ip = input('ip? ').strip()
        res = funcs.ip_locator(ip)
        for key, value in res.items():
            print(key, ':', value)
    elif ans == 'x':
        print('GoodBye')
        break
    else:
        print('hmm?')
    # wait for user
    input('Press any key to continue...')
