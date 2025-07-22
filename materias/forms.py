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

class UsuarioCrearForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['dni', 'first_name', 'last_name', 'email', 'rol', 'career']
        widgets = {
            'dni': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'rol': forms.Select(attrs={'class': 'form-select'}),
            'career': forms.Select(attrs={'class': 'form-select'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['rol'].required = True
        self.fields['career'].required = True