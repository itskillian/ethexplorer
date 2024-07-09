import requests

from ..api_keys import etherscan_api_key

def get_eth_balance(address):
    url = 'https://api.etherscan.io/api'
    # TODO set in environment variables
    api_key = etherscan_api_key
    payload = {
        'module': 'account',
        'action': 'balance',
        'address': address,
        'tag': 'latest',
        'apikey': api_key,
    }
    response = requests.get(url, params=payload)
    data = response.json()
    return data['result']
