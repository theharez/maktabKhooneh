from django.urls import reverse
from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage
from users.forms import user_creation_form
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, HttpResponseRedirect


def login_view(request):                                              
    if not request.user.is_authenticated:
        if request.method == 'POST':
            entry_method = request.POST.get('entry_method')
            password = request.POST.get('password')
            if '@' in entry_method:
                try:
                    entry_method = User.objects.get(email=entry_method)
                    user = authenticate(request, username=entry_method.username, password=password)
                    if user is not None:
                        login(request, user)
                        return redirect('/')
                except:
                    messages.add_message(request, messages.INFO, 'Incorrect username or password')
                    return render(request, 'users/login.html')
            else:
                user = authenticate(request, username=entry_method, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('/')
                else:
                    messages.add_message(request, messages.INFO, 'Incorrect username or password')
                    return render(request, 'users/login.html')
    return render(request, 'users/login.html')


def signup_view(request):
    if not request.user.is_authenticated:
        form = user_creation_form()
        if request.method == 'POST':
            form = user_creation_form(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('users:login'))
            else:
                messages.add_message(request, messages.ERROR, form.errors)
        context = {'form': form}
        return render(request, 'users/signup.html', context)
    else:
        return redirect('/')


@login_required()
def logout_view(request):
    logout(request)
    return redirect('/')


def password_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            entry_method = request.POST.get('entry_method')
            password = request.POST.get('old')
            new = request.POST.get('new')
            confirmation = request.POST.get('confirmation')
            if '@' in entry_method:
                if authenticate(request, username=entry_method.username, password=password):
                    user = User.objects.get(username=entry_method.username)
                    if new == confirmation:
                        user.password = make_password(new)
                        user.save()
                        return HttpResponseRedirect(reverse('users:login'))
                    else:
                        messages.add_message(request, messages.INFO, 'Passwords are not match')
                        return render(request, 'users/password.html')
                else:
                    messages.add_message(request, messages.INFO, 'User is not found')
                    return render(request, 'users/password.html')
            else:
                if authenticate(request, username=entry_method, password=password):
                    user = User.objects.get(username=entry_method)
                    if new == confirmation:
                        user.password = make_password(new)
                        user.save()
                        return HttpResponseRedirect(reverse('users:login'))
                    else:
                        messages.add_message(request, messages.INFO, 'Passwords are not match')
                        return render(request, 'users/password.html')
                else:
                    messages.add_message(request, messages.INFO, 'User is not found')
                    return render(request, 'users/password.html')
        else:
            return render(request, 'users/password.html')
    else:
        return redirect('/')


def email_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user=User.objects.filter(email=email)
        if user:
            user = User.objects.get(email=email)
            note = f'Hi dear {user.username} you asked for reset your passwrod\nTo continue the process please click the below link'
            message = EmailMessage(
                'request for password',
                f'{note}\nhttp://127.0.0.1:8000/users/password\nwebsite admin', 
                settings.EMAIL_HOST_USER,
                [email])
            message.fail_silently=False
            message.send()
            messages.add_message(request, messages.SUCCESS, 'Check your inbox or spam box')
        else:
            messages.add_message(request, messages.ERROR, 'Your email is not valid, Please Try again')
            return HttpResponseRedirect(reverse('users:email'))
    return render(request, 'users/email.html')