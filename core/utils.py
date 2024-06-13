import requests

def get_eth_balance(address):
    url = "https://api.etherscan.io/api"
    # TODO set in environment variables
    api_key = "ZQMABVX6DUEUS98WUDZ9JPC5YXDHQWVAUN"
    payload = {
        "module": "account",
        "action": "balance",
        "address": address,
        "tag": "latest",
        "apikey": api_key
    }
    response = requests.get(url, params=payload)
    data = response.json()
    return data['result']
