from django.urls import path
from website.views import *

urlpatterns = [
    path('', home),
    path('contact', contact),
    path('about', about)
]
