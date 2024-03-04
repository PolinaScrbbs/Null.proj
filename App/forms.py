from django import forms
from .models.models import Direction, Event
from Auth.models import CustomUser

class PhoneNumberForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['phone_number']

    phone_number = forms.CharField(label='Введите ваш номер телефона', widget=forms.TextInput(attrs={'placeholder': 'Номер телефона'}))
    
class CodeForm(forms.Form):
    code = forms.CharField(widget=forms.Textarea(attrs={'class': 'codemirror'}))