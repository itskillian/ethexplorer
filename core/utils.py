import requests

from config.settings import etherscan_api_key

def get_eth_balance(address):
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
    url = 'https://api.etherscan.io/api'
    payload = {
        'module': 'account',
        'action': 'txlist',
        'address': address,
        'startblock': '0',
        'endblock': '99999999',
        'sort': 'asc',
    }
    response = requests.get(url, params=payload)
    return response.json()['result']