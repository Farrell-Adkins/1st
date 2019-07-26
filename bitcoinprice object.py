# pip install requests
import requests

# def crypto_price(name):
#     response = requests.get(f'https://api.coinmarketcap.com/v1/ticker/{name}').json()
#     price_usd = str(response[0]['price_usd'])
#     price = str(f"price is : {price_usd}$")
#     return price

# print(crypto_price("Bitcoin"))

class Crypto:
    
    def __init__(self):
        self.url = 'https://api.coinmarketcap.com/v1/ticker/'
    
    def get_usd_price(self, crypto_name):
        response = self.__request(self.url + crypto_name)
        return str(response[0]['price_usd'])

    def __request(self, url):
        return requests.get(url).json()


crypto_instance = Crypto()
bitcoin_price = crypto_instance.get_usd_price('Bitcoin')
print(f"price is : {bitcoin_price}$")