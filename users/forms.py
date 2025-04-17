from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import User


class UserRegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'form-control mr-0 ml-auto m-2'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control mr-0 ml-auto m-2'})

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2', 'gender', 'age')
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control mr-0 ml-auto m-2'}),
            'username': forms.TextInput(attrs={'class': 'form-control mr-0 ml-auto m-2'}),
            'age': forms.NumberInput(attrs={'class': 'form-control mr-0 ml-auto m-2'}),
            'gender': forms.Select(attrs={'class': 'form-control mr-0 ml-auto m-2', 'style': "width: 360px"}),
        }

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if password1 and len(password1) < 8:
            self.add_error('password1', 'Password must be at least 8 characters long.')
        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        return password2


class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            user = authenticate(email=email, password=password)
            if user is None:
                raise forms.ValidationError("Invalid email or password")
            return self.cleaned_data
