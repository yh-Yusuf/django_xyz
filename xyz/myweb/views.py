from django.shortcuts import render
from django.http import *
from django.http import *
import datetime

def home(request):
    # return HttpResponse("HELLO")
    # d = [3,2,3,4,5]
    # k = {'info': d}
    dt = datetime.datetime.today()
    k = {"info": dt}
    return render(request , 'index.html', k)

def second_page(request):
    return render(request,'second.html')