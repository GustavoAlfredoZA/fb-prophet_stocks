from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import stocks.stockAnalisys
from datetime import date

def index(request):
    #latest_question_list = s
    #context = {'latest_question_list': latest_question_list}
    f = open("stocks/date.txt", "r")
    print(f)
    List = stocks.stockAnalisys.stockL
    args = {}
    args['stock_list'] = List
    args['today'] = date.today()
    return render(request, 'index.html', args)
