from django.shortcuts import render


def login_view(request):
    return render(request, 'users/login.html')

def logout_view(request):
    return render(request, 'users/logout.html')

def singup_view(request):
    return render(request, 'users/singup.html')