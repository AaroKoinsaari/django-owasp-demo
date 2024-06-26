from django.db import models
from django.contrib.auth.models import User
from django import forms


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254, unique=True)
    phone_number = models.CharField(max_length=20, unique=True)
    bio = models.TextField(max_length=500, blank=True)
    # A02:2021 and A07:2021: Passwords stored in plain text, Permits default password (this case even empty)
    password = models.CharField(max_length=128, null=True, blank=True)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username


class RegisterForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, required=True)
    phone_number = forms.CharField(max_length=20, required=True)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['email', 'phone_number', 'bio', 'is_public']

    is_public = forms.BooleanField(required=False, label="Make my profile public!")


class UserSearchForm(forms.Form):
    username = forms.CharField(max_length=150, required=False)
