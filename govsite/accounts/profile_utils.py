"""Utility functions for user profile and login tracking"""
from django.utils import timezone
from .models import LoginHistory


def get_client_ip(request):
    """Extract client IP from request"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def log_login_success(request, user):
    """Log successful login attempt"""
    ip = get_client_ip(request)
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    
    # Update user profile
    profile = user.userprofile
    profile.last_login_ip = ip
    profile.last_login_at = timezone.now()
    profile.failed_login_attempts = 0
    profile.is_account_locked = False
    profile.account_locked_until = None
    profile.save()
    
    # Log to history
    LoginHistory.objects.create(
        user=user,
        ip_address=ip,
        user_agent=user_agent,
        is_successful=True
    )


def log_login_failure(request, user, reason="Invalid credentials"):
    """Log failed login attempt and lock account if needed"""
    ip = get_client_ip(request)
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    
    # Log to history
    LoginHistory.objects.create(
        user=user,
        ip_address=ip,
        user_agent=user_agent,
        is_successful=False,
        failure_reason=reason
    )
    
    # Update failed attempts
    profile = user.userprofile
    profile.failed_login_attempts += 1
    
    # Lock account after 5 failed attempts
    if profile.failed_login_attempts >= 5:
        profile.is_account_locked = True
        profile.account_locked_until = timezone.now() + timezone.timedelta(minutes=15)
    
    profile.save()


def check_account_locked(user):
    """Check if account is locked and unlock if lockout period expired"""
    profile = user.userprofile
    
    if profile.is_account_locked and profile.account_locked_until:
        if timezone.now() > profile.account_locked_until:
            # Unlock account
            profile.is_account_locked = False
            profile.failed_login_attempts = 0
            profile.account_locked_until = None
            profile.save()
            return False
        return True
    return False
