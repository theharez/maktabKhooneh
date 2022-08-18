from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Home page</h1>')

def about(request):
    return HttpResponse('<h1>About us</h1>')
    
def contact(request):
    return HttpResponse('<h1>Contact us</h1>')