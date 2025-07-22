from django import forms
from usuarios.models import User
from .models import Career, Materia

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

class CareerForm(forms.ModelForm):
    class Meta:
        model = Career
        fields = ['name']  # Ajusta si tu modelo Career tiene más campos
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = ['nombre', 'carrera']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'carrera': forms.Select(attrs={'class': 'form-select'}),
        }