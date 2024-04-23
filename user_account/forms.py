from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


# Create User Account Form
class CreateAccountForm(UserCreationForm):
    # Add Attribute Class that are Not inherited by UserCreationForm for Bootstrap class
    first_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    state = forms.ChoiceField(
        choices=CustomUser.STATES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'state', 'username', 'password1', 'password2']
        labels = {
            'password1': 'Password',
            'password2': 'Confirm Password',
        }

    # Add Attribute are inherited from UserCreationForm for Bootstrap class
    def __init__(self, *args, **kwargs):
        super(CreateAccountForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

    # Clean Email Data
    def clean_email(self):
        email = self.cleaned_data['email']

        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists.")
        return email.lower()

    # Clean Email Data
    def clean_username(self):
        username = self.cleaned_data['username']

        if CustomUser.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already exists.")
        return username.lower()


# Login Form
class LoginForm(forms.Form):
    # Add fields and Attribute Class Bootstrap class
    username = forms.CharField(label='Username', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        # Validation for Username and Password
        if not username:
            raise forms.ValidationError("Username is required")
        if not password:
            raise forms.ValidationError("Password is required")

        return cleaned_data


# Update CustomUser Form


# Create and Update Profile Form
