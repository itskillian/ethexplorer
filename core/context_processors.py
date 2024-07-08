import requests

from core.forms import AddressForm
from django.shortcuts import render, redirect

#from core.models import SiteLogo, FooterInfo

def gas_tracker_context(request):
    url = 'https://api.etherscan.io/api'
    # TODO set in environment variables
    api_key = 'ZQMABVX6DUEUS98WUDZ9JPC5YXDHQWVAUN'
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
    api_key = 'ZQMABVX6DUEUS98WUDZ9JPC5YXDHQWVAUN'
    payload = {
        'module': 'stats',
        'action': 'ethprice',
        'apikey': api_key
    }
    response = requests.get(url, params=payload)
    price = response.json()['result']

    return {'price': price}

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