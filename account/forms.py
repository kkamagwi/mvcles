from .models import CustomUser
from django import forms


class LoginForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'password')