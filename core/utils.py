import requests
import time

from config.settings import ETHERSCAN_API_KEY
from decimal import Decimal, InvalidOperation
from requests.exceptions import HTTPError, Timeout, RequestException

current_time_unix = int(time.time())

class APIError(Exception):
    def __init__(self, message):
        super().__init__(message)

def handle_api_errors(url, payload=None):
    try:
        response = requests.get(url, params=payload, timeout=10)
        # raise an HTTPError if status code indicates error (400 and above)
        response.raise_for_status()
        # checks for succesful api call before returning json
        status = response.json()['status']
        if status == '1':
            return response.json()
        elif status == '0':
            raise APIError('API returned a failed status: 0')
        else:
            raise APIError(f'API returned an unkown status: {status}')
    except (HTTPError, Timeout, RequestException, ValueError, Exception) as e:
        raise e


def get_eth_balance(address, url='https://api.etherscan.io/api'):
    """
    Returns the wei balance of a given eth address
    Returns type str
    """
    api_key = ETHERSCAN_API_KEY
    payload = {
        'module': 'account',
        'action': 'balance',
        'address': address,
        'tag': 'latest',
        'apikey': api_key,
    }
    try:
        result = handle_api_errors(url, payload)['result']
        return result
    except Exception as e:
        raise e


def get_normal_txns(address, url='https://api.etherscan.io/api'):
    """
    Returns the list of normal transactions performed by an address
    This API endpoint returns a max of 10,000 records only
    """
    api_key = ETHERSCAN_API_KEY
    payload = {
        'module': 'account',
        'action': 'txlist',
        'address': address,
        'startblock': '0',
        'endblock': '99999999',
        'sort': 'desc',
        'apikey': api_key,
    }
    try:
        result = handle_api_errors(url, payload)['result']
        return result
    except Exception as e:
        return e


def get_eth_price(url='https://api.etherscan.io/api'):
    api_key = ETHERSCAN_API_KEY
    payload = {
        'module': 'stats',
        'action': 'ethprice',
        'apikey': api_key
    }
    try:
        result = handle_api_errors(url, payload)['result']
        return result
    except Exception as e:
        return e


def get_gas_price(url='https://api.etherscan.io/api'):
    api_key = ETHERSCAN_API_KEY
    payload = {
        'module': 'gastracker',
        'action': 'gasoracle',
        'apikey': api_key,
    }
    try:
        result = handle_api_errors(url, payload)['result']
        return result
    except Exception as e:
        return e


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


def get_eth_supply(url='https://api.etherscan.io/api'):
    """
    Returns the total supply of ether
    excluding ETH2 staking rewards and EIP1559 burnt fees
    returns type string
    """
    api_key = ETHERSCAN_API_KEY
    payload = {
        'module': 'stats',
        'action': 'ethsupply2',
        'apikey': api_key,
    }
    try:
        result = handle_api_errors(url, payload)['result']
        return result
    except Exception as e:
        return e


def get_block_num(url='https://api.etherscan.io/api'):
    """
    returns the current block number
    """
    api_key = ETHERSCAN_API_KEY
    payload = {
        'module': 'block',
        'action': 'getblocknobytime',
        'timestamp': current_time_unix,
        'closest': 'before',
        'apikey': api_key,
    }
    try:
        result = handle_api_errors(url, payload)['result']
        return result
    except Exception as e:
        return e


def get_node_count(url='https://api.etherscan.io/api'):
    """
    returns the total number of discoverable Ethereum nodes
    returns dict keys: "UTCDate", "TotalNodeCount"
    """
    api_key = ETHERSCAN_API_KEY
    payload = {
        'module': 'stats',
        'action': 'nodecount',
        'apikey': api_key,
    }
    try:
        result = handle_api_errors(url, payload)['result']
        return result
    except Exception as e:
        return e
