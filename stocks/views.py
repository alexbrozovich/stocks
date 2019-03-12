import json
import requests
import datetime

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import TrackedStock
# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the stocks index.")

def detail(request, ticker_id):
    urlStart = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='
    urlEnd = '&apikey=XX4Q236EB0T9AGVT'
    url = urlStart + ticker_id + urlEnd
    response = requests.get(url)
    data = json.loads(response.text)
    currentDate = str(datetime.datetime.now()).split(' ')[0]
    try:
        openingPrice = str(data['Time Series (Daily)'][currentDate]['1. open'])
    except KeyError:
        latest = list(data['Time Series (Daily)'].keys())[0]
        openingPrice = str(data['Time Series (Daily)'][latest]['1. open'])
        return HttpResponse("%s opened at $%s on Friday (%s)" % (ticker_id, openingPrice, latest))
    return HttpResponse("%s opened at $%s today (%s)" % (ticker_id, openingPrice, currentDate))
    #return HttpResponse(openingPrice)

def tracking(request):
    userID = request.user.username
    all_tracked_list = TrackedStock.objects.all()
    user_tracked = []
    for item in all_tracked_list:
        if str(item.owning_user) == str(userID):
            user_tracked.append(item.ticker)
    context = {
        'user_tracked': user_tracked,
        }
    return render(request, 'tracking/trackedStocks.html', context)

def tracknewstock(request):
    return render(request, 'tracking/tracknewstock.html')
    

def add_tracked_stock(request):
    symbol = request.POST['symbol']
    trackedstock = TrackedStock(ticker=symbol, owning_user=request.user.username)
    trackedstock.save()
    return HttpResponseRedirect(reverse('stocks:tracking'))

def home(request):
    return render(request, 'home.html')

def tracked_graphs(request):
    userID = request.user.username
    all_tracked_list = TrackedStock.objects.all()
    user_tracked = []
    for item in all_tracked_list:
        if str(item.owning_user) == str(userID):
            user_tracked.append(item.ticker)
    user_tracked = user_tracked[2]

    urlStart = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='
    urlEnd = '&apikey=XX4Q236EB0T9AGVT'
    priceData = []
    for ticker_id in user_tracked:
        url = urlStart + ticker_id + urlEnd
        response = requests.get(url)
        data = json.loads(response.text)
        
        priceSeries = []
        #data['Time Series (Daily)'][currentDate]['1. open']
        keys = data['Time Series (Daily)']
        for key in keys:
            priceSeries.append(float(data['Time Series (Daily)'][key]['1. open']))
        priceData = priceSeries

    context = {
        'user_tracked': user_tracked,
        'price_data': priceData,
        }

    return render(request, 'tracking/trackedGraphs.html', context)