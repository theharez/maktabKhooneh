
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class user_creation_form(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
