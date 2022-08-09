import pandas as pd
import requests
import time

portfolio_usdt = 500
profit = 0

def sell():
    url = 'https://api.binance.com/api/v3/ticker/price'
    params = {
    'symbol': 'BTCUSDT'
    }
    response = requests.get(url, params=params)
    data = response.json()
    price = data['price']
    global portfolio_usdt
    global profit
    global balance
    portfolio_usdt = holding*float(price)
    profit = portfolio_usdt - 500
    portfolio_usdt = portfolio_usdt - profit
    balance = portfolio_usdt + profit
    print(f"BTC Sold At ${price} Current Btc Amount is {holding}BTC . Balance is ${balance}. Profit is ${profit}")



def buy():
    url = 'https://api.binance.com/api/v3/ticker/price'
    params = {
    'symbol': 'BTCUSDT'
    }
    response = requests.get(url, params=params)
    data = response.json()
    price = data['price']
    global portfolio_usdt
    global holding
    global profit
    global balance
    holding = portfolio_usdt/int(float(price))
    portfolio_usdt = 0
    balance = portfolio_usdt + profit
    print(f"BTC Bought At ${price} Current Btc Amount is {holding}BTC . Balance is ${balance}. Profit is ${profit}")

while True:
    buy()
    time.sleep(10)
    sell()
