from django.urls import path
from website.views import *

app_name = 'website'
urlpatterns = [
    path('', home_page, name='home_view'),
    path('contact', contact_page, name='contact_view'),
    path('about', about_page, name='about_view'),
    path('news-letter', news_letter_page, name='news_letter')
]
