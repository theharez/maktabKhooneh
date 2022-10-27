from django.http import HttpResponse
from django.shortcuts import HttpResponseRedirect, render
from website.forms import ContactForm, news_letter_form
from django.contrib import messages

""" def home(request):
    return HttpResponse('<h1>Home page</h1>') """
    
    
def home_page(request):
    return render(request, 'main_page/index.html')    

def about_page(request):
    return render(request, 'main_page/about.html')

    
def contact_page(request):
    if request.method == 'POST':
        request.POST._mutable = True
        request.POST['name'] = 'Unkown'
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.add_message(request, messages.SUCCESS, 'Your ticket has been submitted')
            form.save()
        else:
            messages.add_message(request, messages.ERROR, "Your ticket has not been submitted")
    form = ContactForm()
    return render(request, 'main_page/contact.html', {'form': form})


def news_letter_page(request):
    if request.method == 'POST':
        form = news_letter_form(request.POST)
        if form.is_valid():
            messages.add_message(request, messages.SUCCESS, 'We will infrom you')
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')