from django import forms
from usuarios.models import User

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['dni', 'first_name', 'last_name', 'email']
        widgets = {
            'dni': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }