from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, dni, first_name, last_name, email, password = None, rol = 'student', career = None):
        if not dni:
            raise ValueError('El usuario debe tener un DNI valido')
        email = self.normalize_email(email)
        user = self.model(
            dni = dni,
            first_name = first_name,
            last_name = last_name,
            email = email,
            rol = rol,
            career = career
        )
        user.set_password(password if password else dni)
        user.save(using = self._db)
        return user
    
    def create_superuser(self, dni, first_name, last_name, email, password):
        user = self.create_user(
            dni = dni,
            first_name = first_name,
            last_name = last_name,
            email = email,
            password = password,
            rol = 'admin'
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using = self._db)
        return user
    
class User(AbstractBaseUser, PermissionsMixin):
    ROLES = [
        ('admin', 'Administrator'),
        ('student', 'Student'),
    ]

    id = models.AutoField(primary_key = True)
    dni = models.CharField(max_length = 8, unique = True)
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.EmailField(unique = True)
    rol = models.CharField(max_length = 20, choices = ROLES)
    career = models.ForeignKey('materias.Career', on_delete = models.SET_NULL, null = True, blank = True)
    date_joined = models.DateTimeField(default = timezone.now)
    last_login = models.DateTimeField(blank = True, null = True)

    is_active = models.BooleanField(default = True)
    is_superuser = models.BooleanField(default = False)
    is_staff = models.BooleanField(default = False)

    objects = UserManager()

    USERNAME_FIELD = 'dni'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    def save(self, *args, **kwargs):
        if self.rol != 'admin' and self.career is None:
            raise ValueError('Los usuarios deben tener una carrera asociada')
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.dni})'
    
    class Meta:
        indexes = [
            models.Index(fields=['last_name']),
            models.Index(fields=['first_name']),
        ]