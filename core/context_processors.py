import requests

from ..api_keys import etherscan_api_key
from core.forms import AddressForm
from django.shortcuts import render, redirect

#from core.models import SiteLogo, FooterInfo

def gas_tracker_context(request):
    url = 'https://api.etherscan.io/api'
    # TODO set in environment variables
    api_key = etherscan_api_key
    payload = {
        'module': 'gastracker',
        'action': 'gasoracle',
        'apikey': api_key,
    }
    response = requests.get(url, params=payload)
    data = response.json()
    gas = data['result']
    
    return {'gas': gas}


def eth_tracker_context(request):
    url = 'https://api.etherscan.io/api'
    # TODO set in environment variables
    api_key = etherscan_api_key
    payload = {
        'module': 'stats',
        'action': 'ethprice',
        'apikey': api_key
    }
    response = requests.get(url, params=payload)
    result = response.json()['result']
    ethusd = result['ethusd']
    ethbtc = result['ethbtc']

    return {'eth_usd': ethusd, 'eth_btc': ethbtc}

def search_form_context(request):
    # load form
    form = AddressForm(None)

    return {'form':form}

#def logo_context(request):
#    logo = SiteLogo.objects.first()
#    return {'logo': logo}


#def footer_context(request):
#    footer_info = FooterInfo.objects.first()
#    return {'footer_info': footer_info}