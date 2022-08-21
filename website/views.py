from django.http import HttpResponse
from django.shortcuts import render

""" def home(request):
    return HttpResponse('<h1>Home page</h1>') """
    
def home(request):
    return render(request, 'index/index.html')    

def about(request):
    return HttpResponse('<h1>About us</h1>')
    
def contact(request):
    return HttpResponse('<h1>Contact us</h1>')