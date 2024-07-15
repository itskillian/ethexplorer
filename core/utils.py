import requests

from config.settings import etherscan_api_key
from decimal import Decimal, InvalidOperation


def get_eth_balance(address):
    """
    Returns the wei balance of a given eth address
    Returns type str
    """
    url = 'https://api.etherscan.io/api'
    payload = {
        'module': 'account',
        'action': 'balance',
        'address': address,
        'tag': 'latest',
        'apikey': etherscan_api_key,
    }
    response = requests.get(url, params=payload)
    return response.json()['result']


def get_normal_txns(address):
    """
    Returns the list of normal transactions performed by an address
    This API endpoint returns a max of 10,000 records only
    """
    url = 'https://api.etherscan.io/api'
    payload = {
        'module': 'account',
        'action': 'txlist',
        'address': address,
        'startblock': '0',
        'endblock': '99999999',
        'sort': 'desc',
    }
    response = requests.get(url, params=payload)
    return response.json()['result']


def get_eth_price():
    url = 'https://api.etherscan.io/api'
    api_key = etherscan_api_key
    payload = {
        'module': 'stats',
        'action': 'ethprice',
        'apikey': api_key
    }
    response = requests.get(url, params=payload)
    return response.json()['result']


def get_gas_price():
    url = 'https://api.etherscan.io/api'
    api_key = etherscan_api_key
    payload = {
        'module': 'gastracker',
        'action': 'gasoracle',
        'apikey': api_key,
    }
    response = requests.get(url, params=payload)
    return response.json()['result']


def wei_to_eth(value):
    """
    input takes str or int
    converts wei to ETH
    """
    try:
        wei = int(value)
    except ValueError:
        print('error converting str to int')
        raise ValueError('Input must be an int or str representing an int')
    
    eth = wei / 1e18
    return eth


def eth_usd_converter(value, from_currency, to_currency):
    """
    converts between ETH and USD
    """
    try:
        eth_price_str = (get_eth_price()['ethusd'])
        eth_price = Decimal(eth_price_str)
    except (InvalidOperation, TypeError, KeyError):
        raise ValueError('error fetching eth price')
    
    if from_currency == 'ETH' and to_currency == 'USD':
        return value * eth_price
    elif from_currency == 'USD' and to_currency == 'ETH':
        return value / eth_price
    else:
        raise ValueError('Invalid currency pair')
    

def get_eth_supply():
    """
    Returns the total supply of ether
    excluding ETH2 staking rewards and EIP1559 burnt fees
    returns type string
    """
    url = 'https://api.etherscan.io/api'
    api_key = etherscan_api_key
    payload = {
        'module': 'stats',
        'action': 'ethsupply',
        'apikey': api_key,
    }
    response = requests.get(url, params=payload)
    return response.json()['result']