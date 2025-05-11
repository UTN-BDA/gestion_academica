from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from .forms import CustomUserCreationForm

# Register your models here.

class UserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserCreationForm
    model = User

    list_display = ('dni', 'first_name', 'last_name', 'email', 'rol', 'is_staff')
    list_filter = ('rol', 'is_staff', 'is_superuser', 'career')
    fieldsets = (
        (None, {'fields': ('dni', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'career')}),
        ('Permissions', {'fields': ('rol', 'is_staff', 'is_superuser')}),
        ('Dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('dni', 'first_name', 'last_name', 'email', 'career', 'rol'),
        }),
    )
    search_fields = ('dni', 'email', 'first_name', 'last_name')
    ordering = ('dni',)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.set_password(str(obj.dni))
        super().save_model(request, obj, form, change)

admin.site.register(User, UserAdmin)