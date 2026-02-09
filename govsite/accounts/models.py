from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, RegexValidator

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Mobile number validation: exactly 10 digits
    mobile = models.CharField(
        max_length=10, 
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^\d{10}$',
                message='Mobile number must be exactly 10 digits',
                code='invalid_mobile'
            )
        ]
    )

    # OTPs - 6 digit strings
    email_otp = models.CharField(max_length=6, null=True, blank=True)
    mobile_otp = models.CharField(max_length=6, null=True, blank=True)

    # OTP timestamps
    email_otp_created_at = models.DateTimeField(null=True, blank=True)
    mobile_otp_created_at = models.DateTimeField(null=True, blank=True)

    # Verification status
    email_verified = models.BooleanField(default=False)
    mobile_verified = models.BooleanField(default=False)

    # Login activity tracking
    last_login_ip = models.GenericIPAddressField(null=True, blank=True)
    last_login_at = models.DateTimeField(null=True, blank=True)
    failed_login_attempts = models.IntegerField(default=0)
    is_account_locked = models.BooleanField(default=False)
    account_locked_until = models.DateTimeField(null=True, blank=True)

    # Timestamps for tracking
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} - {self.mobile}"


class LoginHistory(models.Model):
    """Track user login activity"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='login_history')
    ip_address = models.GenericIPAddressField()
    login_time = models.DateTimeField(auto_now_add=True)
    user_agent = models.TextField(blank=True)
    is_successful = models.BooleanField(default=True)
    failure_reason = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = "Login History"
        verbose_name_plural = "Login Histories"
        ordering = ['-login_time']

    def __str__(self):
        return f"{self.user.username} - {self.login_time}"
