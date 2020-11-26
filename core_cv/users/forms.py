from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile, GuestProfile

# ? now working on register form


class UserRegisterForm_my(UserCreationForm):

    # using internal function to redefine the builin look
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


# update the user profile

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        # todo update password thru the email (password form)
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


# todo guest contact form
class GuestContactForm(forms.ModelForm):
    class Meta:
        model = GuestProfile
        fields = ['name', 'email', 'message']
