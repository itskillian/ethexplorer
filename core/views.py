# from django.http import JsonResponse
from django.shortcuts import render
# from django.views import View

from core.utils import get_eth_balance

def search(request):
    return render(request, 'core/search.html')


def balance(request):
    address = request.GET.get('faddress')
    balance_wei = int(get_eth_balance(address))
    balance = balance_wei / 1000000000000000000
    context = {"balance": balance}
    return render(request, 'core/search.html', context)