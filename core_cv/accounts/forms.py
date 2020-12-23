from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm_my(UserCreationForm):
    # register regular user build in django functionality 
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm_my, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs["placeholder"] = "Enter Password"
        self.fields['username'].widget.attrs["placeholder"] = "UserName"

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "name": "email",
                "id": "email",
                "placeholder": "Your Email *"
            }
        )
    )
