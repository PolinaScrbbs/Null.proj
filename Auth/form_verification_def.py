from django import forms
from django.apps import apps
from django.db import models

#Наличие данных
def data_availability(label, label_name):
    if not label:
        raise forms.ValidationError(f'{label_name} не может быть пустым')

#Длинна
def length_check(label, label_name, min, max):
    if len(label) < min:
        raise forms.ValidationError(f'{label_name} должно иметь не менее {min} символов')
    elif len(label) > max:
        raise forms.ValidationError(f'{label_name} должно иметь не более {max} символов')

#Проверка наличия символов
def symbols_presence(label, symbols, message):
    if any(symbol in label for symbol in symbols):
        raise forms.ValidationError(f'{message}')

#Проверка отсутствия символов   
def symbols_absence(label, symbols, message):
    if not any(domain in label for domain in symbols):
            raise forms.ValidationError(f'{message}')

#Получение модели из строки  
def get_model_Auth(model_name):
    try:
        model = apps.get_model('Auth', model_name)
        return model
    except LookupError:
        return None

#Состоит только из буквенных символов
def check_string(label, message):
    if any(char.isdigit() for char in label):
        raise forms.ValidationError(f'{message}')
        
#Состоит только из цифр
def check_numeric(label, message):
    if label.isdigit():
        raise forms.ValidationError(f'{message}')

#Проверка на наличие 3 пробелов в строке
def is_full_name(label, message):
    if len(label.split()) != 3:
        raise forms.ValidationError(f'{message}')

#Проверка уникальности в бд
def check_db(model_name, field_name, label, message):
    model = get_model_Auth(model_name)
    if model.objects.filter(**{field_name: label}).exists():
        raise forms.ValidationError(f'{message}')

def name_checker(label, message):
    forbiddens = ['пидор', 'pidor']

    label = label.lower()
    
    for forbidden in forbiddens:
        if forbidden in label:
            raise forms.ValidationError(f'{message}')
    
#Пароль===============================================================================>

def password_data_availability(label, label_name):
    if len(label) == 0:
        raise forms.ValidationError({"password": f'{label_name} не может быть пустым'})

def password_length_check(label, label_name, min, max):
    if len(label) < min:
        raise forms.ValidationError({'password': f'{label_name} должно иметь не менее {min} символов'})
    elif len(label) > max:
        raise forms.ValidationError({'password': f'{label_name} должно иметь не более {max} символов'})

def password_symbols_absence(label, symbols, message):
    if not any(domain in label for domain in symbols):
        raise forms.ValidationError({'password': f'{message}'})
  
def password_equality_check(obj1, obj2, message):
    if obj1 != obj2:
        raise forms.ValidationError({'password': f'{message}'})
    
    


