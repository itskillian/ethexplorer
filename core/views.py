from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
# from django.views import View

from .forms import AddressForm
from .utils import get_eth_balance

def index(request):
    form = AddressForm()
    return render(request, 'core/search.html', {'form': form})


def address(request):
    if request.method == 'GET':
        # create form and populate with GET request data:
        form = AddressForm(request.GET)
        # check whether valid:
        if form.is_valid():
            address = form.cleaned_data['address']    
            balance_wei = int(get_eth_balance(address))
            balance = balance_wei / 1000000000000000000
            context = {
                "balance": balance,
                "address": address,
            }
            return render(request, 'core/address.html', context)
        else:
            return HttpResponse('error')
    
    return render(request, 'core/search.html', context)