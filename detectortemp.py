#!/usr/bin/python3
 #################################
 #      Lucas Rocha Abraao       #
 #     lucasrabraao@gmail.com    #
 #           30/11/2020          #
 #################################
"""
Esse script fica no servidor do zabbix, no diretório:
/lib/zabbix/externalscripts/
"""
import sys
from bs4 import BeautifulSoup
import requests

response = requests.get("ip do ESP 8266 NodeMCU")

bs = BeautifulSoup(response.text, 'html.parser')
temp = bs.find("div", {"class": "temp"})
hum = bs.find("div", {"class": "hum"})
    
if len(sys.argv) < 2:
    print("selecione TEMP ou HUM")
    sys.exit()
if sys.argv[1] == 'temp':
    print(int(float(temp.text)))
elif sys.argv[1] == 'humi':
    print(hum.text)
