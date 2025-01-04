import json
import requests
import time
import hashlib
import hmac

#Global Variables
API_BASE_URL = 'https://api.gateio.ws/api/v4'

#generate signature
def gen_sign(API_KEY, API_SECRET, method, url, query_string=None, payload_string=None):
    t = time.time()
    m = hashlib.sha512()
    m.update((payload_string or "").encode('utf-8'))
    hashed_payload = m.hexdigest()
    s = '%s\n%s\n%s\n%s\n%s' % (method, url, query_string or "", hashed_payload, t)
    sign = hmac.new(API_SECRET.encode('utf-8'), s.encode('utf-8'), hashlib.sha512).hexdigest()
    return {'KEY': API_KEY, 'Timestamp': str(t), 'SIGN': sign}

#feth the total current balance
def fetch_total_balance(API_KEY, API_SECRET):
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    url = '/wallet/total_balance'
    query_param = ''

    #generate signature
    sign_headers = gen_sign(API_KEY, API_SECRET,'GET', prefix + url, query_param)
    headers.update(sign_headers)

    #get request
    response = requests.request('GET', host + prefix + url, headers=headers)
    return float(response.json()['total']['amount'])


#fetch all currency pairs
def fetch_currecy_pair():
    url = f"{API_BASE_URL}/spot/currency_pairs"
    response = requests.get(url)
    if response.status_code == 200:
        pairs = [pair['id'] for pair in response.json()]
        return pairs
    else:
        print("Error fetching currency pairs")

def fetch_currecy_pair_price(currency):
    url = f"{API_BASE_URL}/spot/tickers?currency_pair={currency+"_USDT"}"
    response = requests.get(url)
    if response.status_code == 200:
        return float(response.json()[0]['last'])
    else:
        print("Error fetching market price:", response.json())
        return None

#fetch the available amount of currency in assets
def fetch_asset_amount(API_KEY, API_SECRET, currency):
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    url = '/spot/accounts'
    query_param = ''
    
    #generatie signature
    sign_headers = gen_sign(API_KEY, API_SECRET,'GET', prefix + url, query_param)
    headers.update(sign_headers)
    
    #get request
    response = requests.request('GET', host + prefix + url, headers=headers)
    for coin in response.json():
        if currency == coin['currency']:
            return coin['available']
    return 0


#buy currency pair for an amount in USD and a price of the currency
def buy_currency(API_KEY, API_SECRET, currency, amount, price):
    prefix = "/api/v4"
    url = '/spot/orders'
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    query_param = ''
    body = json.dumps({
        "text":"t-123456",
        "currency_pair": currency+"_USDT",
        "type":"market",
        "account":"spot",
        "side":"buy",
        "iceberg": 0,
        "amount": amount,
        "price": price,
        "time_in_force": "fok",
        "auto_borrow": False
    })
    sign_headers = gen_sign(API_KEY, API_SECRET, 'POST', prefix + url, query_param, body)
    headers.update(sign_headers)
    response = requests.request('POST', API_BASE_URL + url, headers=headers, data=body)
    return response.json()

#sell maximum of currency pair
def sell_max_currency(API_KEY, API_SECRET, currency):
    prefix = "/api/v4"
    url = '/spot/orders'
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    query_param = ''
    body = json.dumps({
        "text":"t-123456",
        "currency_pair": currency+"_USDT",
        "type":"market",
        "account":"spot",
        "side":"sell",
        "amount": fetch_asset_amount(API_KEY, API_SECRET, currency),
        "time_in_force": "ioc",
        "auto_borrow": False
    })
    sign_headers = gen_sign(API_KEY, API_SECRET, 'POST', prefix + url, query_param, body)
    headers.update(sign_headers)
    response = requests.request('POST', API_BASE_URL + url, headers=headers, data=body)
    return response.json()
