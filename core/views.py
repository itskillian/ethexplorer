from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
# from django.views import View

from .forms import AddressForm
from .utils import get_eth_balance

def index(request):
    # load form and get submitted data
    form = AddressForm(request.GET)
    # check whether valid:
    if form.is_valid():
        address = form.cleaned_data['address']
        return redirect('core:address', address=address)
    else:
        return render(request, 'core/search.html', {'form': AddressForm()})


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