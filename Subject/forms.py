from django import forms
from .models import User

from .form_verification_def import data_availability, length_check, check_string, check_numeric, symbols_presence, symbols_absence, check_db, is_full_name, name_checker
from .form_verification_def import password_data_availability, password_length_check, password_symbols_absence, password_equality_check

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'full_name', 'email', 'password', 'password_check', 'agree_to_terms', 'mailing']

    username = forms.CharField(label='username', widget=forms.TextInput(attrs={'placeholder': 'Имя.Unique()', 'image_url': '/media/auth/user.svg'}))
    full_name = forms.CharField(label='Полное имя', widget=forms.TextInput(attrs={'placeholder': 'Полное_имя.Split()', 'image_url': '/media/auth/user.svg'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'placeholder': 'E-mail', 'image_url': '/media/auth/email.svg'}))
    
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'placeholder': 'Пароль', 'image_url': '/media/auth/password.svg'}))
    password_check = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'placeholder': 'Подтвердите пароль', 'image_url': '/media/auth/password.svg'}))
    
    agree_to_terms = forms.BooleanField(label='Создавая аккаунт, вы соглашаетесь с нашей политикой конфидециальности', required=True)
    mailing = forms.BooleanField(label='Согласиться на спам', required=False)

    def clean_username(self):
        forbidden_symbols = ('!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+', '=', '[', ']', '{', '}', ';', ':', ',', '<', '>', '/', '?', '|', '\\')
        email_domains = ['@gmail.com', '@mail.ru', '@yandex.ru', '@inbox.ru', '@ok.ru', '@rambler.ru']
        allowed_symbols = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890'
        username = self.cleaned_data['username']
        
        data_availability(username, 'Имя пользователя')
        length_check(username, 'Имя пользователя', 4, 20)
        check_numeric(username, 'Имя пользователя не может состоять только из цифр')
        symbols_absence(username, allowed_symbols, 'Никнейм может содержать только английские буквы и цифры')
        symbols_presence(username, forbidden_symbols, 'Поле может содержать только буквы и цифры')
        symbols_presence(username, email_domains, 'Поле не может содержать домен почты')
        name_checker(username, 'Поле содержит запрещённые слова')
        check_db('User', 'username', username, 'Пользователь с таким именем уже зарегистрирован')
        
        return username

    def clean_email(self):
        email_domains = ['@gmail.com', '@mail.ru', '@yandex.ru', 'inbox.ru', 'ok.ru', 'rambler.ru']
        email = self.cleaned_data['email']
        
        data_availability(email, 'Электронная почта')
        symbols_absence(email, email_domains, 'Формат электронной почты не верный')
        check_db('User', 'email', email, 'Пользователь с таким e-mail уже зарегистрирован')

        return email

    def clean_full_name(self):
        full_name = self.cleaned_data['full_name']
        allowed_symbols = 'йцукенгшщзхъфывапролджэячсмитьёЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'
        
        data_availability(full_name, 'ФИО')
        symbols_absence(full_name, allowed_symbols, 'Имя может содержать только Русские буковы')
        name_checker(full_name, 'Поле содержит запрещённые слова')
        is_full_name(full_name,'Введите ваше ФИО через пробел')
        
        return full_name.title()
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data['password']
        password_check = cleaned_data['password_check']

        allowed_symbols = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

        password_data_availability(password, 'Пароль')
        password_length_check(password, 'Пароль', 8, 24)
        password_symbols_absence(password, allowed_symbols, 'Поле может содержать только латинские буквы и цифры')
        password_equality_check(password, password_check, 'Пароли не совпадают')
        
        agree_to_terms = cleaned_data.get('agree_to_terms')

        if not agree_to_terms:
            raise forms.ValidationError({'agree_to_terms': 'Для продолжения необходимо согласиться с условиями'})

        return cleaned_data
    
    # def __init__(self, *args, **kwargs):
    #     super(RegistrationForm, self).__init__(*args, **kwargs)
    #     for name, field in self.fields.items():
    #         print(f"Field name: {name}, Image URL: {field.widget.attrs.get('image_url')}")



