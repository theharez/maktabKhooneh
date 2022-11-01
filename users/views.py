from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm


def login_view(request):
    """ if request.method == 'POST':
        username = request.POST['username']        
        password = request.POST['password'] 
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:    
            return render(request, 'users/login.html') """
    
    form = AuthenticationForm()
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user:
                    login(request, user)
                    return redirect('/')
        context = {'from': form}
        return render(request, 'users/login.html', context)
    else:
        return redirect('/')

def logout_view(request):
    return render(request, 'users/logout.html')

def singup_view(request):
    return render(request, 'users/singup.html')