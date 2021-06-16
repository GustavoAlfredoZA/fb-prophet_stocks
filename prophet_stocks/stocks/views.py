from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from django.views.generic.edit import CreateView
from django import forms
from django.template.loader import render_to_string
from django.views.generic import TemplateView
import stocks.stockAnalysis
import datetime
from datetime import date
from threading import Thread
from stocks.forms import FundamentalForm
from stocks.FAnalysis import *
from stocks.TAnalysis import *



def index(request):
    #latest_question_list = s
    #context = {'latest_question_list': latest_question_list}
    f = open("stocks/date.txt", "r")
    file = f.read().split('-')
    datefile = date(int(file[0]),int(file[1]),int(file[2]))

    List = stocks.stockAnalysis.stockL
    args = {}
    args['stock_list'] = List
    args['today'] = date.today()
    if(date.today().weekday()>5):
        return render(request, 'index.html', args)
    elif(datefile != date.today() and datetime.datetime.now().hour > 16):
        thread = Thread(target = stocks.stockAnalysis.runAnalysis)
        thread.start()
        f = open("stocks/date.txt", "w")
        f.write(str(date.today()))
        f.close()
    return render(request, 'index.html', args)

class FundamentalView(TemplateView):
    template_name = 'metrics.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = FundamentalForm()

        return context

    def post(self, request, *args, **kwargs):
        strStocks = request.POST.get('Ticker')
        stocks = strStocks.split(' ')
        return JsonResponse(
            {
                'content': {
                    'message': FA(stocks),
                }
            }
        )
