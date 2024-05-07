from django import forms
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm

from .models import CustomUser, Profile


# Create User Account Form
class CreateAccountForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove the "password is too similar to the last name" validator
        self.fields['password1'].validators = []
        self.fields['password2'].validators = []

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

    def __init__(self, *args, **kwargs):
        super(CreateAccountForm, self).__init__(*args, **kwargs)
        # Add Attribute are inherited from UserCreationForm for Bootstrap class
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

        # Set custom help text for password1 field
        self.fields['password1'].help_text = (
            "<ul>"
            "<li>Use at least 8 characters.</li>"
            "<li>Use uppercase and lowercase characters.</li>"
            "<li>Use at least one number.</li>"
            "<li>At least use one special character (!@#$%^&*).</li>"
            "</ul>"
        )

    # Clean Email Data
    def clean_email(self):
        email = self.cleaned_data['email']

        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists.")
        return email.lower()

    # Clean Username Data
    def clean_username(self):
        username = self.cleaned_data['username']

        if CustomUser.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already exists.")
        return username.lower()

    # Custom password validation
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        # Custom password validation logic
        if len(password1) < 8:
            raise forms.ValidationError("Password must be at least 8 characters long.")
        if not any(char.isupper() for char in password1):
            raise forms.ValidationError("Password must contain at least one uppercase letter.")
        if not any(char.islower() for char in password1):
            raise forms.ValidationError("Password must contain at least one lowercase letter.")
        if not any(char.isdigit() for char in password1):
            raise forms.ValidationError("Password must contain at least one digit.")
        if not any(char in '!@#$%^&*' for char in password1):
            raise forms.ValidationError("Password must contain at least one special character (!@#$%^&*).")

        return password1


def clean_password2(self):
    password1 = self.cleaned_data.get("password1")
    password2 = self.cleaned_data.get("password2")
    if password1 and password2 and password1 != password2:
        raise forms.ValidationError(
            self.error_messages['password_mismatch'],
            code='password_mismatch',
        )

    return password2


# Update Password
class CustomSetPasswordForm(SetPasswordForm):
    # Custom password validation
    def clean_new_password1(self):
        password1 = self.cleaned_data.get('new_password1')

        # Custom password validation logic
        if len(password1) < 8:
            raise forms.ValidationError("Password must be at least 8 characters long.")
        if not any(char.isupper() for char in password1):
            raise forms.ValidationError("Password must contain at least one uppercase letter.")
        if not any(char.islower() for char in password1):
            raise forms.ValidationError("Password must contain at least one lowercase letter.")
        if not any(char.isdigit() for char in password1):
            raise forms.ValidationError("Password must contain at least one digit.")
        if not any(char in '!@#$%^&*' for char in password1):
            raise forms.ValidationError("Password must contain at least one special character (!@#$%^&*).")

        return password1

    def clean_new_password2(self):
        password1 = self.cleaned_data.get("new_password1")
        password2 = self.cleaned_data.get("new_password2")

        # Check if passwords match
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )

        return password2

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set custom help text for password1 field
        self.fields['new_password1'].help_text = (
            "<ul>"
            "<li>Use at least 8 characters.</li>"
            "<li>Use uppercase and lowercase characters.</li>"
            "<li>Use at least one number.</li>"
            "<li>At least use one special character (!@#$%^&*).</li>"
            "</ul>"
        )


# Profile
# Create and Update Profile Form
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['display_name', 'avatar', 'player_bio']

    # Clean Display Name Data
    def clean_display_name(self):
        display_name = self.cleaned_data['display_name']

        # Check if the display name already exists excluding the current instance
        existing_display_name = Profile.objects.filter(display_name=display_name).exclude(pk=self.instance.pk)
        if existing_display_name.exists():
            raise forms.ValidationError("Display Name already exists.")
        return display_name.lower()


# Update CustomUser Form
class UserUpdateForm(forms.ModelForm):
    # Add Fields to Update CustomUser Form
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    first_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    state = forms.ChoiceField(
        choices=CustomUser.STATES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'state']

    # Add Attribute Class to existing Fields for Bootstrap
    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
