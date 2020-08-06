from django import forms
#from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from django.forms import TextInput, EmailInput, Select, FileInput
from user.models import UserProfile
from crispy_forms.helper import FormHelper

from django.contrib.auth import get_user_model
User = get_user_model()

#from .models import Order


class OrderForm(ModelForm):
	class Meta:
		#model = Order
		fields = '__all__'

class CreateUserForm(UserCreationForm):
    
	class Meta:
	    model = User
	    fields = ['email',  'password1', 'password2']


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['email']
        widgets = {
            'username'  : TextInput(attrs={'class': 'input','placeholder':'username'}),
            'email'     : EmailInput(attrs={'class': 'input','placeholder':'email'}),
            'first_name': TextInput(attrs={'class': 'input','placeholder':'first_name'}),
            'last_name' : TextInput(attrs={'class': 'input','placeholder':'last_name' }),
        }


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone', 'address1', 'city','country')
        widgets = {
            'phone'     : TextInput(attrs={'class': 'input','placeholder':'phone'}),
            'address'   : TextInput(attrs={'class': 'input','placeholder':'address'}),
            'city'      : Select(attrs={'class': 'input','placeholder':'city'}),
            'country'   : TextInput(attrs={'class': 'input','placeholder':'country' }),
        }
