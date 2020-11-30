import urllib.request
from bs4 import BeautifulSoup

def temp_hum(config):
    IP = config.get_ip()
    response = urllib.request.urlopen(f'http://{IP}:4200/') #ip temporário
    #soup = BeautifulSoup(response.read(), from_encoding=response.headers.getparam('charset'))
    soup = BeautifulSoup(response.read(), features="lxml")

    temp = None
    for line in soup.find('div', {'class': 'temp'}).stripped_strings:
        temp = line
    hum = None
    for line in soup.find('div', {'class': 'hum'}).stripped_strings:
        hum = line
    
    return temp, hum

if __name__ == '__main__':
    temp, hum = temp_hum(config)
    print(temp, hum)