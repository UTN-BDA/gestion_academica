from django import forms
from .models import User

class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('dni', 'first_name', 'last_name', 'email', 'career', 'rol')

    def save(self, commit = True):
        user = super().save(commit = False)
        user.set_password(str(user.dni))
        if commit:
            user.save()
        return user