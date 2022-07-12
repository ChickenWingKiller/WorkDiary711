from django import forms

from .models import User

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('name', 'username', 'email', 'password')

class UserFormLogin(forms.ModelForm):
    username = forms.CharField(label='用户名', max_length=100)
    # password = forms.CharField(label='密码', widget=forms.PasswordInput())
    password = forms.CharField(label='密码')
    class Meta:
        model = User
        fields = ('username', 'password')