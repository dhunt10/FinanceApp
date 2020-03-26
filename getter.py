import requests
import bs4
from bs4 import BeautifulSoup
from colors import bcolors
import dateutil


def quoteGetter(stock):
    """

    """
    URL = 'https://finance.yahoo.com/quote/{}?p={}'.format(stock, stock)
    prev = 0
    value = 0
    try:
         r = requests.get(URL)
         soup = bs4.BeautifulSoup(r.text, 'html.parser')
         prev = value
         value = float(soup.find_all('div', {'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text.encode('ascii', 'ignore'))
    except(ValueError):
        print(bcolors.FAIL + 'Stock is not yet acceptable')

    return (value)
