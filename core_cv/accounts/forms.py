from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class MyUser(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'image', 'role')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'image')


# class TenantForm(UserCreationForm):
#     class Meta:
#         model = Tenant
#         fields = ('username', 'email', 'image', 'apartment')
