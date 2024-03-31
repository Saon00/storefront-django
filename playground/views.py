from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def say_hello(req):
    return render(req, 'index.html')
    # return HttpResponse('Saon Srabon')

def add(request):
    return HttpResponse("1+1")