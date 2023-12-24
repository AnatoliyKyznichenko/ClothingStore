from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.forms import PasswordInput
from user.models import CustomUser


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', max_length=150)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Пароль', widget=PasswordInput)
    password2 = forms.CharField(label='Повторите Пароль', widget=PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        if CustomUser.objects.filter(username=username).exists():
            raise forms.ValidationError('Пользователь с таким именем уже существует')
        return username

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', max_length=150)
    password = forms.CharField(label='Пароль', widget=PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('username', 'password')