import requests

from config.settings import etherscan_api_key


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


def get_eth_price(request):
    url = 'https://api.etherscan.io/api'
    api_key = etherscan_api_key
    payload = {
        'module': 'stats',
        'action': 'ethprice',
        'apikey': api_key
    }
    response = requests.get(url, params=payload)
    return response.json()['result']

def get_gas_price(request):
    url = 'https://api.etherscan.io/api'
    api_key = etherscan_api_key
    payload = {
        'module': 'gastracker',
        'action': 'gasoracle',
        'apikey': api_key,
    }
    response = requests.get(url, params=payload)
    return response.json()['result']

def convert_wei(value):
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