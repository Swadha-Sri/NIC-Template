from django.core.mail import send_mail
from django.contrib.auth.models import User
import random
import re
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

# ============ OTP Functions ============
def generate_otp():
    """Generate a random 6-digit OTP"""
    return str(random.randint(100000, 999999))

def send_email_otp(email, otp):
    """Send OTP via email with error handling"""
    subject = 'Government Portal - OTP Verification'
    message = f'''
Dear User,

Your OTP for verification is:

{otp}

Do not share this OTP with anyone.
This OTP is valid for 10 minutes.

Regards,
Government Portal
'''

    try:
        # Send email
        result = send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False
        )
        
        if result == 0:
            logger.warning(f"Email not sent to {email} - no recipients")
            raise Exception("Email could not be sent")
            
        logger.info(f"OTP sent successfully to {email}")
        return True
        
    except Exception as e:
        logger.error(f"Failed to send OTP to {email}: {str(e)}")
        # Log the OTP for debugging in development
        logger.debug(f"[DEBUG] OTP for {email}: {otp}")
        raise Exception(f"Failed to send OTP: {str(e)}")

def send_sms_otp(mobile, otp):
    """
    Replace this logic with:
    - NIC SMS Gateway
    - BSNL SMS API
    - Twilio (testing)
    """
    print(f"[SMS OTP] Mobile: {mobile}, OTP: {otp}")


# ============ Validation Functions ============
def validate_email(email):
    """
    Validate email format
    Returns: (is_valid: bool, error_message: str)
    """
    if not email:
        return False, "Email is required"
    
    # Email regex pattern
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if not re.match(email_pattern, email):
        return False, "Invalid email format"
    
    if len(email) > 254:
        return False, "Email is too long"
    
    return True, ""


def validate_mobile(mobile):
    """
    Validate mobile number (10 digits)
    Returns: (is_valid: bool, error_message: str)
    """
    if not mobile:
        return False, "Mobile number is required"
    
    # Remove any non-digit characters
    mobile_digits = re.sub(r'\D', '', mobile)
    
    if len(mobile_digits) != 10:
        return False, "Mobile number must be 10 digits"
    
    if not mobile_digits.isdigit():
        return False, "Mobile number must contain only digits"
    
    return True, ""


def validate_username(username):
    """
    Validate username format
    Returns: (is_valid: bool, error_message: str)
    """
    if not username:
        return False, "Username is required"
    
    if len(username) < 3:
        return False, "Username must be at least 3 characters long"
    
    if len(username) > 30:
        return False, "Username must be at most 30 characters long"
    
    # Username can contain letters, numbers, underscores
    username_pattern = r'^[a-zA-Z0-9_]+$'
    
    if not re.match(username_pattern, username):
        return False, "Username can only contain letters, numbers, and underscores"
    
    if User.objects.filter(username=username).exists():
        return False, "Username already exists"
    
    return True, ""


def validate_password(password, confirm_password=None):
    """
    Validate password strength
    Returns: (is_valid: bool, error_message: str)
    """
    if not password:
        return False, "Password is required"
    
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"
    
    if len(password) > 128:
        return False, "Password is too long"
    
    # Check for at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return False, "Password must contain at least one uppercase letter"
    
    # Check for at least one lowercase letter
    if not re.search(r'[a-z]', password):
        return False, "Password must contain at least one lowercase letter"
    
    # Check for at least one digit
    if not re.search(r'[0-9]', password):
        return False, "Password must contain at least one digit"
    
    # Check for at least one special character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False, "Password must contain at least one special character (!@#$%^&*)"
    
    if confirm_password is not None and password != confirm_password:
        return False, "Passwords do not match"
    
    return True, ""


def validate_name(name):
    """
    Validate user's name
    Returns: (is_valid: bool, error_message: str)
    """
    if not name:
        return False, "Name is required"
    
    if len(name) < 2:
        return False, "Name must be at least 2 characters long"
    
    if len(name) > 100:
        return False, "Name is too long"
    
    # Name can contain letters and spaces only
    name_pattern = r'^[a-zA-Z\s]+$'
    
    if not re.match(name_pattern, name):
        return False, "Name can only contain letters and spaces"
    
    return True, ""


def validate_otp(otp):
    """
    Validate OTP format
    Returns: (is_valid: bool, error_message: str)
    """
    if not otp:
        return False, "OTP is required"
    
    if len(otp) != 6:
        return False, "OTP must be 6 digits"
    
    if not otp.isdigit():
        return False, "OTP must contain only digits"
    
    return True, ""


# ============ User Lookup Functions ============
def get_user_by_email(email):
    """
    Get user by email
    Returns: (user_object or None, error_message: str)
    """
    try:
        user = User.objects.get(email=email)
        return user, ""
    except User.DoesNotExist:
        return None, "User with this email does not exist"
    except Exception as e:
        return None, f"An error occurred: {str(e)}"


def email_exists(email):
    """Check if email already exists"""
    return User.objects.filter(email=email).exists()


def username_exists(username):
    """Check if username already exists"""
    return User.objects.filter(username=username).exists()
