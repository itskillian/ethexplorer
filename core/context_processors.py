import requests

from core.forms import AddressForm
from core.utils import get_eth_price, get_gas_price
# from django.shortcuts import render, redirect

#from core.models import SiteLogo, FooterInfo

def gas_price_context(request):
    gas_data = get_gas_price()
    return {'gas_context': gas_data}


def eth_price_context(request):
    eth_data = get_eth_price()
    return {'eth_context': eth_data}

def search_form_context(request):
    # load form
    search_form = AddressForm(None)

    return {'search_form':search_form}

#def logo_context(request):
#    logo = SiteLogo.objects.first()
#    return {'logo': logo}


#def footer_context(request):
#    footer_info = FooterInfo.objects.first()
#    return {'footer_info': footer_info}