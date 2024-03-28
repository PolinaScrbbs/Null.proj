from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


#Субъекты (Пользователь или организация)
# class Subject(models.Model):
#     title = models.CharField(max_length=20, unique=True, verbose_name='Название')
    
#     class Meta:
#         verbose_name = 'Субъект'
#         verbose_name_plural = 'Субъекты' 
    
#     def __str__(self):
#         return self.title

#Роли (Администратор, модератор, пользователь)  
class Role(models.Model):
    title = models.CharField(max_length=20, unique=True, verbose_name='Роль')
    
    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли' 
    
    def __str__(self):
        return self.title

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not username:
            raise ValueError('The username field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        admin_role = Role.objects.get(id=1)
        extra_fields.setdefault('role', admin_role)

        return self.create_user(username, email, password, **extra_fields)

#Пользователи
class User(AbstractBaseUser, PermissionsMixin):
    avatar = models.ImageField(upload_to='user_avatars', blank=True, null=True, verbose_name='Аватарка')
    username = models.CharField(max_length=50, unique=True, blank=False, verbose_name='Уникальное имя')
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, blank=True, default=3, null=True, verbose_name='Роль')
    full_name = models.CharField(max_length=100, blank=False, verbose_name='Полное имя')
    email = models.EmailField(unique=True, blank=False, verbose_name='E-mail')
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name='Номер телефона')
    mailing = models.BooleanField(verbose_name='Согласие на рассылку', default=False)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'full_name']

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


