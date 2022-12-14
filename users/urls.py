from django.urls import path
from users.views import *

app_name = 'users'
urlpatterns = [
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('signup', signup_view, name='signup'),
    path('email', email_view, name='email'),
    path('password', password_view, name='password')
]