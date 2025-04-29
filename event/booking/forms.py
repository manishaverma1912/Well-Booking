from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['name', 'username', 'email', 'mobile', 'address', 'password1', 'password2']


# this is latest user registeration form
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    name = forms.CharField(max_length=100, required=True)
    mobile = forms.CharField(max_length=15, required=True)
    address = forms.CharField(widget=forms.Textarea, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'name', 'email', 'mobile', 'address', 'password1', 'password2')

# this is for the event booking
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_type', 'date', 'time', 'catering', 'people_count', 'special_requests']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'special_requests': forms.Textarea(attrs={'rows': 3}),
        }

from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'phone', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'contactus', 'placeholder': 'Name'}),
            'phone': forms.TextInput(attrs={'class': 'contactus', 'placeholder': 'Phone'}),
            'email': forms.EmailInput(attrs={'class': 'contactus', 'placeholder': 'Email'}),
            'message': forms.Textarea(attrs={'class': 'textarea', 'placeholder': 'Message'}),
        }
