from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
# from django.views import View

from .context_processors import eth_tracker_context
from .forms import AddressForm
from .models import Txn
from .utils import get_eth_balance, get_normal_txns

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
    
    txn_data = get_normal_txns(address)

    for data in txn_data:
        t, created = Txn.objects.get_or_create(
            transaction_hash = data['hash'],
            defaults={
                'block_number' : data['blockNumber'],
                'timestamp' : data['timeStamp'],
                'nonce' : data['nonce'],
                'block_hash' : data['blockHash'],
                'transaction_index' : data['transactionIndex'],
                'from_address' : data['from'],
                'to_address' : data['to'],
                'value' : data['value'],
                'gas' : data['gas'],
                'gas_price' : data['gasPrice'],
                'is_error' : data['isError'],
                'txreceipt_status' : data['txreceipt_status'],
                'input' : data['input'],
                'contract_address' : data['contractAddress'],
                'cumulative_gas_used' : data['cumulativeGasUsed'],
                'gas_used' : data['gasUsed'],
                'confirmations' : data['confirmations'],
                'method_id' : data['methodId'],
                'function_name' : data['functionName'],
            }
        )
        if not created:
            print('duplicate found, skipping over')


    context = {
        'eth_balance': eth_balance,
        'eth_value': eth_value,
        'address': address,
    }
    return render(request, 'core/address.html', context)


def error(request):
    error = 'An error has occured'
    return render(request, 'core/error.html', {'error': error})