 #################################
 #      Lucas Rocha Abraao       #
 #     lucasrabraao@gmail.com    #
 #           30/11/2020          #
 #################################

class Config:
    __IP = "192.168.0.1" # ip do arduino NodeMCU. Variável privada
    
    @staticmethod # pra pegar a variável privada
    def get_ip():
        return Config.__IP

# Pra usar:
#from config import Config
#print(Config.get_ip())
