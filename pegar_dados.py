import urllib.request
from bs4 import BeautifulSoup

def temp_hum(config):
    IP = config.get_ip()
    try:
        response = urllib.request.urlopen(f'http://{IP}:4200/', timeout=3) #ip temporário
    except:
        return 404
    #soup = BeautifulSoup(response.read(), from_encoding=response.headers.getparam('charset'))
    #soup = BeautifulSoup(response.read(), features="lxml")
    soup = BeautifulSoup(response.read(), "html.parser")

    temp = None
    for line in soup.find('div', {'class': 'temp'}).stripped_strings:
        temp = line
    hum = None
    for line in soup.find('div', {'class': 'hum'}).stripped_strings:
        hum = line
    
    return {
        "response": response,
        "temp": float(temp),
        "hum": float(hum)
    }

if __name__ == '__main__':
    temp, hum = temp_hum(config)
    print(temp, hum)
