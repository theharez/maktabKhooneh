from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse



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

@login_required()
def logout_view(request):
    logout(request)
    return redirect('/')
    

def signup_view(request):
    if not request.user.is_authenticated:
        form = UserCreationForm()
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('users:login'))
        context = {'form': form}
        return render(request, 'users/signup.html', context)
    else:
        return redirect('/')