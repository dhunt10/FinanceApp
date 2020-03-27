import tkinter as tk
from tkinter import *
import os

def changeColor(label):
    label.config(bg='cyan')
    label.update()

def client():
    quote = input("Enter a stock symbol").upper()
    prev = 0
    value = 0
    wndw = tk.Tk()
    label1 = Label(wndw, bd=8, relief='solid', font='Times 22 bold', bg='black', fg='white', text='welcome')
    label1.config(padx=0, pady=0)
    B = tk.Button(wndw, text='chnage color', command=changeColor(label1))
    B.pack()
    label1.pack()
    wndw.title(quote)
    up = True
    while True:
        prev = value
        value = float(os.popen('curl' + ' --fail --silent ' + 'http://127.0.0.1:8080/trade\?stock\={}'.format(quote)).read())
        if value > prev:
            up = True
            label1.config(text=str(value), fg='green', bg='black')
            label1.update()
        elif value < prev:
            up = False
            label1.config(text=str(value), fg='red', bg='black')
            label1.update()
        else:
            label1.config(text=str(value), fg='white')
            if up:
                label1.config(bg='green')
            else:
                label1.config(bg='red')
            label1.update()

if __name__ == '__main__':
    client()
