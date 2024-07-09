from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
# from django.views import View

from .context_processors import eth_tracker_context
from .forms import AddressForm
from .utils import get_eth_balance

def index(request):
    # load form
    form = AddressForm(request.GET or None)
    # check whether any data submitted via GET:
    #if any(request.GET.values()):
    if form.is_valid():
        # redirect to address view, passing address as arg
        address = form.cleaned_data['address']
        return redirect('core:address', address=address)
    else:
        # form has no data, load empty form template
        return render(request, 'core/index.html', {'form': form})
    

def address(request, address):
    try:
        wei_balance = int(get_eth_balance(address))
    except ValueError:
        print('redirecting to error view')
        return redirect('core:error')
    eth_balance = wei_balance * pow(10, -18)
    eth_usd = eth_tracker_context(request)['eth_usd']
    eth_value = eth_balance * float(eth_usd)
    context = {
        'eth_balance': eth_balance,
        'eth_value': eth_value,
        'address': address,
    }
    return render(request, 'core/address.html', context)


def error(request):
    error = 'An error has occured'
    return render(request, 'core/error.html', {'error': error})