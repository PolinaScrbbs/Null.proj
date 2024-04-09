from django.test import TestCase
from django.urls import reverse
from .forms import RegistrationForm

class RegistrationFormTestCase(TestCase):
    # Тест на верную валидацию формы
    def test_registration_form_valid_data(self):
        form_data = {
            'username': 'PolinaScrbbs',
            'full_name': 'Ивановский Тимофей Владиславович',
            'email': 'polinascaraboobs@gmail.com',
            'password': 'password123',
            'password_check': 'password123',
            'agree_to_terms': True,
            'mailing': False,
        }
        form = RegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())
        
    # Тест на валидацию формы с неверным форматом username
    def test_registration_form_username_language_error(self):
        form_data = {
            'username': 'ПолинаСкрббс',
            'full_name': 'Ивановский Тимофей Владиславович',
            'email': 'polinascaraboobs@gmail.com',
            'password': 'password123',
            'password_check': 'password123',
            'agree_to_terms': True,
            'mailing': False
        }
        form = RegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())
        if form.errors:
            error_message = form.errors.as_text()
            print(f"Ошибка: {error_message}")
            
    # Тест на валидацию формы с запрещёнными словами username
    def test_registration_form_username_forbidden_words(self):
        form_data = {
            'username': 'piDor232',
            'full_name': 'Ивановский Тимофей Владиславович',
            'email': 'polinascaraboobs@gmail.com',
            'password': 'password123',
            'password_check': 'password123',
            'agree_to_terms': True,
            'mailing': False
        }
        form = RegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())
        if form.errors:
            error_message = form.errors.as_text()
            print(f"Ошибка: {error_message}")

    # Тест на валидацию формы с неверным форматом fullname
    def test_registration_form_fullname_format_error(self):
        form_data = {
            'username': 'PolinaScrbbs',
            'full_name': 'ИвановскийТимофейВладиславович',
            'email': 'polinascaraboobs@gmail.com',
            'password': 'password123',
            'password_check': 'password123',
            'agree_to_terms': True,
            'mailing': False
        }
        form = RegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())
        if form.errors:
            error_message = form.errors.as_text()
            print(f"Ошибка: {error_message}")
            
    # Тест на валидацию формы с неверным форматом fullname
    def test_registration_form_fullname_language_error(self):
        form_data = {
            'username': 'PolinaScrbbs',
            'full_name': 'Ivanovskiy Timofey Vladislavivich',
            'email': 'polinascaraboobs@gmail.com',
            'password': 'password123',
            'password_check': 'password123',
            'agree_to_terms': True,
            'mailing': False
        }
        form = RegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())
        if form.errors:
            error_message = form.errors.as_text()
            print(f"Ошибка: {error_message}")
            
    # Тест на валидацию формы с неверным форматом email
    def test_registration_form_email_format_error(self):
        form_data = {
            'username': 'PolinaScrbbs',
            'full_name': 'Ивановский Тимофей Владиславович',
            'email': 'polinascaraboobs@mail.com',
            'password': 'password123',
            'password_check': 'password123',
            'agree_to_terms': True,
            'mailing': False
        }
        form = RegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())
        if form.errors:
            error_message = form.errors.as_text()
            print(f"Ошибка: {error_message}")
    
    # Тест на валидацию формы с разными паролями
    def test_registration_form_different_password(self):
        form_data = {
            'username': 'PolinaScrbbs',
            'full_name': 'Ивановский Тимофей Владиславович',
            'email': 'polinascaraboobs@gmail.com',
            'password': 'password123',
            'password_check': 'differentpassword123',
            'agree_to_terms': True,
            'mailing': False
        }
        form = RegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())
        if form.errors:
            error_message = form.errors.as_text()
            print(f"Ошибка: {error_message}")
            
    # Тест на валидацию формы неверным форматом пароля
    def test_registration_form_password_error(self):
        form_data = {
            'username': 'PolinaScrbbs',
            'full_name': 'Ивановский Тимофей Владиславович',
            'email': 'polinascaraboobs@gmail.com',
            'password': '123',
            'password_check': '123',
            'agree_to_terms': True,
            'mailing': False
        }
        form = RegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())
        if form.errors:
            error_message = form.errors.as_text()
            print(f"Ошибка: {error_message}")
        
    # Тест на валидацию формы с непоставленыым agree_to_terms
    def test_registration_form_undelivered_agree_to_terms(self):
        form_data = {
            'username': 'PolinaScrbbs',
            'full_name': 'Ивановский Тимофей Владиславович',
            'email': 'polinascaraboobs@gmail.com',
            'password': 'password123',
            'password_check': 'password123',
            'agree_to_terms': False,
            'mailing': False
        }
        form = RegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())
        if form.errors:
            error_message = form.errors.as_text()
            print(f"Ошибка: {error_message}")
        
    def test_registration_view(self):
        url = reverse('registration')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration.html')
