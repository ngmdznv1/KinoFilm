from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Comment, Profile


class LoginForm(AuthenticationForm):
    username = forms.CharField(label=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Имя пользователя'
    }))

    password = forms.CharField(label=False, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Пароль'
    }))

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(label=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Имя'
    }))

    last_name = forms.CharField(label=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Фамилия'
    }))

    email = forms.EmailField(label=False, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Почта'
    }))

    username = forms.CharField(label=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Логин'
    }))

    password1 = forms.CharField(label=False, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Пароль'
    }))

    password2 = forms.CharField(label=False, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Подтвердите пароль'
    }))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')



class CommentForm(forms.ModelForm):
    text = forms.CharField(label=False, widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Введите комментарий'
    }))

    class Meta:
        model = Comment
        fields = ('text',)

class EditAccountForm(UserChangeForm):
    first_name = forms.CharField(label=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Имя'
    }))

    last_name = forms.CharField(label=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Фамилия'
    }))

    email = forms.EmailField(label=False, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Почта'
    }))

    username = forms.CharField(label=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Логин'
    }))

    old_password = forms.CharField(required=False, label='Текущий пароль', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Пароль'
    }))

    new_password = forms.CharField(required=False, label='Новый пароль', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Подтвердите пароль'
    }))

    confirm_password = forms.CharField(required=False, label='Подтвердить новый пароль', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Подтвердите пароль'
    }))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'old_password', 'new_password', 'confirm_password')


class EditProfileForm(forms.ModelForm):
    profile_name = forms.CharField(label='Имя профиля', widget=forms.TextInput(attrs={
       'class': 'form-control'
    }))

    nickname = forms.CharField(label='Никнейм профиля', widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    avatar = forms.ImageField(required=False, label='Фото профиля', widget=forms.FileInput(attrs={
        'class': 'form-control'
    }))

    class Meta:
        model = Profile
        fields = ('profile_name', 'nickname', 'avatar')