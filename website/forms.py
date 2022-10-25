from django import forms
from website.models import Contact, news_letter
from captcha.fields import CaptchaField


class ContactForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Contact
        fields = '__all__'

class news_letter_form(forms.ModelForm):
    class Meta:
        model = news_letter
        fields = '__all__'
