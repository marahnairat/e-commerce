from ecommerceApp.services.CurrencyService import CurrencyService
import requests


class CoinDeskServiceClass(CurrencyService.CurrencyServiceClass):
    request = 'https://api.coindesk.com/v1/bpi/currentprice.json'

    def get_currency(self):
        price = requests.get(self.request)
        print(price.json())

        return price
