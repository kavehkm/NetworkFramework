# standard
import socket
# internal
import settings as s
# external
import requests


def port_scan(ip, port):
    is_open = False
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = s.connect_ex((ip, port))
    if result == 0:
        is_open = True
    s.close()
    return is_open


def dns_lookup(hostname, ext=False):
    if ext:
        return socket.gethostbyname_ex(hostname)
    else:
        return socket.gethostbyname(hostname)


def ip_locator(ip):
    url = 'http://api.ipapi.com/{}'.format(ip)
    params = {'access_key': s.ACCESS_KEY}
    res = requests.get(url, params=params).json()
    return {
        'ip': res['ip'],
        'ip_type': res['type'],
        'continent': res['continent_name'],
        'country': res['country_name'],
        'region': res['region_name'],
        'city': res['city'],
        'latitude': res['latitude'],
        'longitude': res['longitude']
    }
