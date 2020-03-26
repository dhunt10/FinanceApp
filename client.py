import getter
from getter import quoteGetter
import Tkinter as tk
import colors
from colors import bcolors
from datetime import datetime
import subprocess
import os

def client():
    quote = raw_input("Enter a stock symbol").upper()
    prev = 0
    value = 0
    while True:
        prev = value
	value = os.popen('curl' + ' --fail --silent ' + 'http://127.0.0.1:8080/trade\?stock\={}'.format(quote)).read()
	if value > prev:
            print(bcolors.OKAY + str(value))
        elif value < prev:
            print(bcolors.FAIL + str(value))
        else:
            print(bcolors.RESET + str(value))

if __name__ == '__main__':
    client()
