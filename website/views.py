from django.http import HttpResponse
from django.shortcuts import render

""" def home(request):
    return HttpResponse('<h1>Home page</h1>') """
    
def home_page(request):
    return render(request, 'main_page/index.html')    

def about_page(request):
    return render(request, 'main_page/about.html')
    
def contact_page(request):
    return render(request, 'main_page/contact.html')