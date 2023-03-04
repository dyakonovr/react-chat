from django.forms import ModelForm, ValidationError
from django import forms
from .models import User


class LogInForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Username', 'class': 'form-input'}), required=True)
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password', 'class': 'form-input'}), required=True, min_length=8)


class SignUpForm(ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={"placeholder": "Password"}), min_length=8, required=True)
    password2 = forms.CharField(
        label='Confirm password', widget=forms.PasswordInput(attrs={"placeholder": "Confirm password"}), min_length=8, required=True)
    error_css_class = 'message-error'
    error_messages = {
        'password_mismatch': 'Passwords must match.',
    }

    class Meta:
        model = User
        fields = ('username', 'email', 'phoneNumber', 'password')
        widgets = {
            "username": forms.TextInput(
                attrs={
                    "placeholder": "Username"
                }
            ),
            "email": forms.TextInput(
                attrs={
                    "placeholder": "Email"
                }
            ),
            "phoneNumber": forms.TextInput(
                attrs={
                    "placeholder": "Phone number (with a country code) ",
                    "type": "tel",
                    "minlength": 12,
                    "maxlength": 12,
                },
            ),
        }

    def clean(self):
        cleaned_data = super(SignUpForm, self).clean()
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("password2")
        if password and confirm_password:
            if password != confirm_password:
                self.add_error(None, "Passwords don't match")
        ifNums = False
        ifLets = False
        for letter in password:
            if letter.isalpha():
                ifLets = True
            if letter.isdigit():
                ifNums = True
            if ifNums == True and ifLets == True:
                break
        if ifNums == False or ifLets == False:
            self.add_error(
                "password", "Your password must contain at least one digit and one letter!")
        return cleaned_data
