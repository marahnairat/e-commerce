import json
from collections import ChainMap


def create_code_rate(con):
    return {con["code"]: con["rate_to_usd"]}


def get_countries():
    jsonfile = open("C:/Users/marah/env_site/ecommerceProject/ecommerceApp/countriesCurrencies.json", "r")
    countries_currencies = json.load(jsonfile)
    countries_currencies = countries_currencies['countries']
    countries_codes = list(map(create_code_rate, countries_currencies))
    return countries_codes


def get_usd_rate(self):
    countries_codes = get_countries()
    countries_codes = dict(ChainMap(*countries_codes))
    usd_rate = countries_codes[self.country_code]
    return usd_rate
