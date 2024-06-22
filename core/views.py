from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

# from django.views import View

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
        return redirect(reverse('core:address', args=[address]))
    else:
        # form has no data, load empty form template
        return render(request, 'core/index.html', {'form': form})
    

def address(request, address):
    try:
        balance_wei = int(get_eth_balance(address))
    except ValueError:
        return HttpResponse('Error! Invalid address format')
    balance = balance_wei / 1000000000000000000
    context = {
        "balance": balance,
        "address": address,
    }
    return render(request, 'core/address.html', context)
