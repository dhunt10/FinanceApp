import requests
import bs4
from bs4 import BeautifulSoup
from colors import bcolors
import dateutil


def quoteGetter(stock):
    """

    """
    final = ""
    stock_list = stock.split()
    for item in stock_list:
        print("ITEM: {}".format(item))
        URL = 'https://finance.yahoo.com/quote/{}?p={}'.format(item, item)
        prev = 0
        value = 0
        try:
             r = requests.get(URL)
             soup = bs4.BeautifulSoup(r.text, 'html.parser')
             prev = value
             value = float(soup.find_all('div', {'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text.encode('ascii', 'ignore'))
        except(ValueError):
            print(bcolors.FAIL + 'Stock is not yet acceptable')
        except(IndexError):
            print("Out of Data")
        final = final + item + ": " + str(value) + " "
    return (final)
