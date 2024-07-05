import requests

#from core.models import SiteLogo, FooterInfo

def gas_tracker_context(request):
    url = "https://api.etherscan.io/api"
    # TODO set in environment variables
    api_key = "ZQMABVX6DUEUS98WUDZ9JPC5YXDHQWVAUN"
    payload = {
        'module': 'gastracker',
        'action': 'gasoracle',
        'apikey': api_key,
    }
    response = requests.get(url, params=payload)
    data = response.json()
    gas = data['result']
    gas_base_fee = gas['suggestBaseFee']
    gas_price = gas['ProposeGasPrice']
    
    return {'gas': gas}


#def logo_context(request):
#    logo = SiteLogo.objects.first()
#    return {'logo': logo}


#def footer_context(request):
#    footer_info = FooterInfo.objects.first()
#    return {'footer_info': footer_info}