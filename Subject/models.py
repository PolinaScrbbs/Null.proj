from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

#Роли (Администратор, модератор, пользователь)  
class Role(models.Model):
    title = models.CharField(max_length=20, unique=True, verbose_name='Роль')

    class Meta:
        abstract = True
    
    def __str__(self):
        return self.title
    
#ПОЛЬЗОВАТЕЛЬ===============================================================================================>

#Роль пользователя
class UserRole(Role):
    class Meta:
        verbose_name = 'Роль пользователя'
        verbose_name_plural = 'Роли пользователей' 

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
        admin_role = UserRole.objects.get(id=1)
        extra_fields.setdefault('role', admin_role)

        return self.create_user(username, email, password, **extra_fields)

#Пользователи
class User(AbstractBaseUser, PermissionsMixin):
    avatar = models.ImageField(upload_to='user_avatars', blank=True, null=True, verbose_name='Аватарка')
    username = models.CharField(max_length=50, unique=True, blank=False, verbose_name='Уникальное имя')
    role = models.ForeignKey(UserRole, on_delete=models.SET_NULL, blank=True, default=3, null=True, verbose_name='Роль')
    full_name = models.CharField(max_length=100, blank=False, verbose_name='Полное имя')
    email = models.EmailField(unique=True, blank=False, verbose_name='E-mail')
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name='Номер телефона')
    mailing = models.BooleanField(verbose_name='Согласие на рассылку', default=False)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'full_name']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username

#ОРГАНИЗАЦИЯ===============================================================================================>

#Роль участника организации
class OrganizationMemberRole(Role):
    class Meta:
        verbose_name = 'Роль в организации'
        verbose_name_plural = 'Роли в организации' 

#Организации
class Organization(models.Model):
    avatar = models.ImageField(upload_to='organization_avatars', blank=True, null=True, verbose_name='Аватарка')
    name = models.CharField(max_length=50, unique=True, blank=False, verbose_name='Уникальное название')
    full_title = models.CharField(max_length=100, blank=False, verbose_name='Полное название')
    description = models.TextField(blank=True, verbose_name='Описание')
    email = models.EmailField(unique=True, blank=False, verbose_name='E-mail')
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name='Номер телефона')

    #Количество участников
    @property
    def members_number(self):
        return OrganizationMember.objects.all().count()
    
    #Получить создателя
    @property
    def owner(self):
        return OrganizationMember.objects.get(role=OrganizationMemberRole.objects.get(id=1))

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации' 
    
    def __str__(self):
        return self.name

#Участник организации
class OrganizationMember(models.Model):
    user = models.ForeignKey(get_user_model(), verbose_name='Пользователь', on_delete=models.CASCADE)
    role = models.ForeignKey(OrganizationMemberRole, verbose_name='Роль', on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, verbose_name='Организация', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Участник организации'
        verbose_name_plural = 'Участники организации'

    def __str__(self):
        return self.user.username