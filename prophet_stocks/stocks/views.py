from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import stocks.stockAnalisys
import datetime
from datetime import date

def index(request):
    #latest_question_list = s
    #context = {'latest_question_list': latest_question_list}
    f = open("stocks/date.txt", "r")
    file = f.read().split('-')
    datefile = date(int(file[0]),int(file[1]),int(file[2]))

    List = stocks.stockAnalisys.stockL
    args = {}
    args['stock_list'] = List
    args['today'] = date.today()
    if(date.today().weekday()>5):
        return render(request, 'index.html', args)
    elif(datefile != date.today() and datetime.datetime.now().hour > 16):
        stocks.stockAnalisys.runAnalisys()
        f = open("stocks/date.txt", "w")
        f.write(str(date.today()))
        f.close()
    return render(request, 'index.html', args)
