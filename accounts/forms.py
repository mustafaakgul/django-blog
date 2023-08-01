from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class RegisterForm(forms.Form):
    username = forms.CharField(max_length = 100, label = "Username")
    # Widget as a password view
    password = forms.CharField(max_length = 20, label = "Password", widget = forms.PasswordInput)
    password_confirm = forms.CharField(max_length = 20, label = "Confirm Password", widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
        ]

    # Runs Before Submit
    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        password_confirm = self.cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords not matched")

        values = {
            "username" : username,
            "password" : password
        }
        return values


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label = "Username")
    password = forms.CharField(max_length=100, label = "Password", widget = forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Username or password is invalid")
        return super(LoginForm, self).clean()
