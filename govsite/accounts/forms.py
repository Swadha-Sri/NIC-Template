from django import forms
from captcha.fields import CaptchaField
from django.contrib.auth.models import User
from .models import UserProfile
from .utils import (
    validate_email, validate_password, validate_mobile,
    validate_name, validate_username
)


class RegistrationForm(forms.Form):
    """Form for user registration with validation"""
    
    username = forms.CharField(
        max_length=30,
        min_length=3,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username',
            'autocomplete': 'username'
        })
    )
    
    name = forms.CharField(
        max_length=100,
        min_length=2,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Full Name',
            'autocomplete': 'name'
        })
    )
    
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email Address',
            'autocomplete': 'email'
        })
    )
    
    mobile = forms.CharField(
        max_length=10,
        min_length=10,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '10-digit Mobile Number',
            'autocomplete': 'tel',
            'type': 'tel'
        })
    )
    
    password = forms.CharField(
        max_length=128,
        min_length=8,
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'autocomplete': 'new-password'
        })
    )
    
    confirm_password = forms.CharField(
        max_length=128,
        min_length=8,
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm Password',
            'autocomplete': 'new-password'
        })
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        is_valid, error_msg = validate_username(username)
        if not is_valid:
            raise forms.ValidationError(error_msg)
        return username

    def clean_name(self):
        name = self.cleaned_data.get('name')
        is_valid, error_msg = validate_name(name)
        if not is_valid:
            raise forms.ValidationError(error_msg)
        return name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        is_valid, error_msg = validate_email(email)
        if not is_valid:
            raise forms.ValidationError(error_msg)
        
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already registered")
        
        return email

    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')
        is_valid, error_msg = validate_mobile(mobile)
        if not is_valid:
            raise forms.ValidationError(error_msg)
        
        if UserProfile.objects.filter(mobile=mobile).exists():
            raise forms.ValidationError("Mobile number already registered")
        
        return mobile

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if password and confirm_password:
            is_valid, error_msg = validate_password(password, confirm_password)
            if not is_valid:
                raise forms.ValidationError(error_msg)
        
        return cleaned_data


class LoginForm(forms.Form):
    """Form for user login"""
    
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email Address',
            'autocomplete': 'email'
        })
    )
    
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'autocomplete': 'current-password'
        })
    )
    
    remember_me = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input'
        })
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        is_valid, error_msg = validate_email(email)
        if not is_valid:
            raise forms.ValidationError(error_msg)
        return email


class LoginCaptchaForm(forms.Form):
    captcha = CaptchaField()


class ProfileEditForm(forms.Form):
    """Form for editing user profile"""
    
    first_name = forms.CharField(
        max_length=100,
        min_length=2,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'First Name'
        })
    )
    
    last_name = forms.CharField(
        max_length=100,
        min_length=2,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Last Name'
        })
    )
    
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email Address'
        })
    )
    
    mobile = forms.CharField(
        max_length=10,
        min_length=10,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '10-digit Mobile Number',
            'type': 'tel'
        })
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        is_valid, error_msg = validate_email(email)
        if not is_valid:
            raise forms.ValidationError(error_msg)
        return email

    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')
        is_valid, error_msg = validate_mobile(mobile)
        if not is_valid:
            raise forms.ValidationError(error_msg)
        return mobile


class ChangePasswordForm(forms.Form):
    """Form for changing user password"""
    
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Current Password'
        })
    )
    
    new_password = forms.CharField(
        max_length=128,
        min_length=8,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'New Password (min 8 characters)'
        })
    )
    
    confirm_password = forms.CharField(
        max_length=128,
        min_length=8,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm New Password'
        })
    )

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get('new_password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if new_password and confirm_password:
            is_valid, error_msg = validate_password(new_password, confirm_password)
            if not is_valid:
                raise forms.ValidationError(error_msg)
        
        return cleaned_data


class OTPVerificationForm(forms.Form):
    """Form for OTP verification"""
    
    otp = forms.CharField(
        max_length=6,
        min_length=6,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '6-digit OTP',
            'autocomplete': 'off',
            'inputmode': 'numeric'
        })
    )

    def clean_otp(self):
        otp = self.cleaned_data.get('otp')
        
        if not otp.isdigit():
            raise forms.ValidationError("OTP must contain only digits")
        
        if len(otp) != 6:
            raise forms.ValidationError("OTP must be exactly 6 digits")
        
        return otp
