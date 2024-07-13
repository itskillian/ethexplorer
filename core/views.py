from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
# from django.views import View

from .context_processors import eth_tracker_context
from .forms import AddressForm, ConversionForm
from .models import Txn
from .utils import eth_usd_converter, get_eth_balance, get_normal_txns, wei_to_eth

def index(request):
    # load form
    search_form = AddressForm(request.GET or None)
    # check whether any data submitted via GET:
    #if any(request.GET.values()):
    if search_form.is_valid():
        # redirect to address view, passing address as arg
        address = search_form.cleaned_data['address']
        return redirect('core:address', address=address)
    else:
        # form has no data, load empty form template
        return render(request, 'core/index.html', {'search_form': search_form})


def conversion(request):
    if request.method == 'GET':
        conversion_form = ConversionForm()
        return render(request, 'core/conversion.html', {'conversion_form': conversion_form})
    elif request.method == 'POST':
        conversion_form = ConversionForm(request.POST)
        if conversion_form.is_valid():
            amount = conversion_form.cleaned_data['amount']
            from_currency = conversion_form.cleaned_data['from_currency']
            to_currency = conversion_form.cleaned_data['to_currency']
            converted_amount = eth_usd_converter(amount, from_currency, to_currency)
            return JsonResponse({'converted_amount': converted_amount})
        else:
            return JsonResponse({'error': 'Invalid form'}, status=400)


def address(request, address):
    # fetch balance data
    try:
        eth_balance = wei_to_eth(get_eth_balance(address))
    except ValueError:
        print('value error, address not valid')
        return redirect('core:error')
    
    # fetch eth price data
    eth_usd = eth_tracker_context(request)['eth_data']['ethusd']
    
    
    eth_value = eth_balance * float(eth_usd)
    
    # fetch transaction data
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
            print('duplicate entry found, skipping over')

    # convert wallet balance from wei to eth
    # TODO make this into a custom template filter
    for txn in txn_data:
        txn['value'] = wei_to_eth(txn['value'])
    
    context = {
        'eth_balance': eth_balance,
        'eth_value': eth_value,
        'address': address,
        'txn_data': txn_data,
    }
    return render(request, 'core/address.html', context)


def error(request):
    error = 'An error has occured'
    return render(request, 'core/error.html', {'error': error})