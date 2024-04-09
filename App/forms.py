from django import forms
from Subject.models import User

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'full_name', 'email', 'phone_number']

    username = forms.CharField(required=False, label='Введите имя пользователя', widget=forms.TextInput(attrs={'placeholder': '@Username'}))
    full_name = forms.CharField(required=False, label='Введите ФИО', widget=forms.TextInput(attrs={'placeholder': 'ФИО'}))
    email = forms.EmailField(required=False, label='Введите Email', widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    phone_number = forms.CharField(required=False, label='Введите ваш номер телефона', widget=forms.TextInput(attrs={'placeholder': 'Номер телефона'}))

    def init(self, *args, **kwargs):
        super(ProfileForm, self).init(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance:
            self.fields['username'].initial = instance.username
            self.fields['full_name'].initial = instance.full_name
            self.fields['email'].initial = instance.email
            self.fields['phone_number'].initial = instance.phone_number

class CodeForm(forms.Form):
    code = forms.CharField(widget=forms.Textarea(attrs={'class': 'codemirror'}))