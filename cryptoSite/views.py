from django.shortcuts import render
import requests
import json

def home(request):  
    api_request= requests.get('https://min-api.cryptocompare.com/data/v2/news/?lang=EN')
    
    api = json.loads(api_request.content)

    return render(request, 'home.html', {'api':api})

def pricing(request):
    price_request = requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,:TC&tsyms=USD')
    
    price = json.loads(price_request.content)

    return render(request, 'pricing.html', {'price':price})




