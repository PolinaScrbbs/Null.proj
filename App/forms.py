from django import forms
from .models.models import Direction, Event
from Auth.models import CustomUser

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'date', 'direction']
        
    title = forms.CharField(label='Название события', widget=forms.TextInput(attrs={'placeholder': 'Введите название события'}))
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'Выберите дату'}),
    )

    direction = forms.ModelChoiceField(queryset=Direction.objects.none(), empty_label='Выберите направление')

    def __init__(self, user, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['direction'].queryset = Direction.objects.filter(creator = user)

class PhoneNumberForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['phone_number']

    phone_number = forms.CharField(label='Введите ваш номер телефона', widget=forms.TextInput(attrs={'placeholder': 'Номер телефона'}))
    
class CodeForm(forms.Form):
    code = forms.CharField(widget=forms.Textarea(attrs={'class': 'codemirror'}))