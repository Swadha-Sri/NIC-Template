from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import UserProfile
from .utils import (
    generate_otp, send_email_otp, send_sms_otp,
    validate_email, validate_password, validate_mobile, 
    validate_name, validate_username, validate_otp,
    get_user_by_email, email_exists, username_exists
)
from .forms import LoginCaptchaForm
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('login-email', '').strip()
        password = request.POST.get('login-pwd', '').strip()
        remember_me = request.POST.get('remember')
        entered_otp = request.POST.get('login_email_otp', '').strip()

        def _login_session_context():
            return {
                "login_email": request.session.get("login_email", ""),
                "login_remember": request.session.get("login_remember", False)
            }

        def _base_context():
            context = {
                "captcha_form": LoginCaptchaForm()
            }
            context.update(_login_session_context())
            return context

        if not entered_otp:
            captcha_form = LoginCaptchaForm(request.POST)
            if not captcha_form.is_valid():
                context = _base_context()
                context.update({"error": "Invalid captcha. Please try again."})
                return render(request, "public/index.html", context)

        # OTP verification step
        if entered_otp:
            # Validate OTP format
            otp_valid, otp_error = validate_otp(entered_otp)
            if not otp_valid:
                context = _base_context()
                context.update({
                    "show_login_email_otp": True,
                    "error": otp_error
                })
                return render(request, "public/index.html", context)

            user_id = request.session.get('otp_user_id')
            if not user_id:
                messages.error(request, 'Session expired. Please login again.')
                return redirect("index")

            try:
                user = User.objects.get(id=user_id)
                profile = user.userprofile
            except User.DoesNotExist:
                messages.error(request, 'User not found. Please login again.')
                return redirect("index")
            except UserProfile.DoesNotExist:
                messages.error(request, 'User profile not found. Please contact support.')
                return redirect("index")

            # Check OTP expiry (10 minutes)
            if timezone.now() > profile.email_otp_created_at + timedelta(minutes=10):
                messages.error(request, 'OTP expired. Please login again.')
                return redirect("index")
            
            # Verify OTP
            if entered_otp != profile.email_otp:
                context = _base_context()
                context.update({
                    "show_login_email_otp": True,
                    "error": "Invalid OTP"
                })
                return render(request, "public/index.html", context)
            
            # Clear OTP and login user
            profile.email_otp = None
            profile.email_otp_created_at = None
            profile.save()

            login(request, user)

            if remember_me:
                request.session.set_expiry(60*60*24*30)  # 30 days

            for key in ["login_email", "login_remember"]:
                request.session.pop(key, None)
            
            messages.success(request, f'Welcome back, {user.first_name}!')
            return redirect('dashboard')
        
        # Initial login step - validate email and password
        email_valid, email_error = validate_email(email)
        if not email_valid:
            context = _base_context()
            context.update({"error": email_error})
            return render(request, "public/index.html", context)
        
        if not password:
            context = _base_context()
            context.update({"error": "Password is required"})
            return render(request, "public/index.html", context)

        # Get user by email
        user, user_error = get_user_by_email(email)
        if not user:
            context = _base_context()
            context.update({"error": user_error})
            return render(request, "public/index.html", context)

        # Check if user account is active
        if not user.is_active:
            context = _base_context()
            context.update({"error": "Your account is not activated. Please complete registration."})
            return render(request, "public/index.html", context)

        # Authenticate user
        user_auth = authenticate(
            request,
            username=user.username,
            password=password
        )

        if not user_auth:
            context = _base_context()
            context.update({"error": "Invalid email or password"})
            return render(request, "public/index.html", context)
        
        # Generate and send OTP
        try:
            otp = generate_otp()
            profile = user.userprofile
            profile.email_otp = otp
            profile.email_otp_created_at = timezone.now()
            profile.save()

            send_email_otp(user.email, profile.email_otp)
        except Exception as e:
            import logging
            logger = logging.getLogger(__name__)
            logger.error(f"OTP sending failed: {str(e)}")
            context = _base_context()
            context.update({
                "error": f"Failed to send OTP: {str(e)}. Please check your email configuration and try again."
            })
            return render(request, "public/index.html", context)

        request.session['otp_user_id'] = user.id
        request.session['otp_purpose'] = 'login'

        request.session["login_email"] = email
        request.session["login_remember"] = bool(remember_me)

        messages.success(request, 'OTP sent to your email.')
        context = _base_context()
        context.update({
            "show_login_email_otp": True
        })
        return render(request, "public/index.html", context)
    
    return redirect('index')


def register_view(request):
    if request.method == 'POST':
        entered_email_otp = request.POST.get('email_otp', '').strip()
        entered_mobile_otp = request.POST.get('mobile_otp', '').strip()

        def _signup_session_context():
            return {
                "signup_username": request.session.get("signup_username", ""),
                "signup_name": request.session.get("signup_name", ""),
                "signup_email": request.session.get("signup_email", ""),
                "signup_mobile": request.session.get("signup_mobile", ""),
            }

        # Initial registration step - collect user data
        if not entered_email_otp and not entered_mobile_otp:
            username = request.POST.get('signup-username', '').strip()
            name = request.POST.get('signup-name', '').strip()
            email = request.POST.get('signup-email', '').strip()
            mobile = request.POST.get('signup-mobile', '').strip()
            password = request.POST.get('signup-pwd', '').strip()
            confirm_password = request.POST.get('signup-confirm-pwd', '').strip()

            request.session["signup_username"] = username
            request.session["signup_name"] = name
            request.session["signup_email"] = email
            request.session["signup_mobile"] = mobile

            # Validate all fields
            name_valid, name_error = validate_name(name)
            if not name_valid:
                return render(request, "public/index.html", {"error": name_error})

            username_valid, username_error = validate_username(username)
            if not username_valid:
                return render(request, "public/index.html", {"error": username_error})

            email_valid, email_error = validate_email(email)
            if not email_valid:
                return render(request, "public/index.html", {"error": email_error})

            if email_exists(email):
                return render(request, "public/index.html", {"error": "Email already registered"})

            mobile_valid, mobile_error = validate_mobile(mobile)
            if not mobile_valid:
                return render(request, "public/index.html", {"error": mobile_error})

            if UserProfile.objects.filter(mobile=mobile).exists():
                return render(request, "public/index.html", {"error": "Mobile number already registered"})

            password_valid, password_error = validate_password(password, confirm_password)
            if not password_valid:
                return render(request, "public/index.html", {"error": password_error})

            # Create user and profile
            try:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password,
                    first_name=name,
                    is_active=False
                )
                
                otp = generate_otp()
                profile = UserProfile.objects.create(
                    user=user,
                    mobile=mobile,
                    email_otp=otp,
                    email_otp_created_at=timezone.now()
                )
                
                send_email_otp(user.email, profile.email_otp)
                
                request.session['otp_user_id'] = user.id
                request.session['otp_step'] = 'email'

                messages.success(request, 'Verification code sent to your email.')
                context = {
                    "show_email_otp": True,
                    "email": email
                }
                context.update(_signup_session_context())
                return render(request, "public/index.html", context)
            except Exception as e:
                messages.error(request, f'Registration failed: {str(e)}')
                return render(request, "public/index.html", {"error": "An error occurred during registration"})

        # Email OTP verification step
        if entered_email_otp and not entered_mobile_otp:
            otp_valid, otp_error = validate_otp(entered_email_otp)
            if not otp_valid:
                context = {
                    "error": otp_error,
                    "show_email_otp": True
                }
                context.update(_signup_session_context())
                return render(request, "public/index.html", context)

            user_id = request.session.get('otp_user_id')
            if not user_id:
                return redirect("index")

            try:
                profile = UserProfile.objects.get(user_id=user_id)
            except UserProfile.DoesNotExist:
                return redirect("index")

            # Check OTP expiry (10 minutes)
            if timezone.now() > profile.email_otp_created_at + timedelta(minutes=10):
                context = {
                    "error": "OTP expired. Please register again.",
                    "show_email_otp": True
                }
                context.update(_signup_session_context())
                return render(request, "public/index.html", context)

            # Verify email OTP
            if entered_email_otp != profile.email_otp:
                context = {
                    "error": "Invalid Email OTP",
                    "show_email_otp": True
                }
                context.update(_signup_session_context())
                return render(request, "public/index.html", context)
            
            # Mark email as verified and generate mobile OTP
            profile.email_verified = True
            profile.email_otp = None
            profile.email_otp_created_at = None

            mobile_otp = generate_otp()
            profile.mobile_otp = mobile_otp
            profile.mobile_otp_created_at = timezone.now()
            profile.save()

            # For development: log/print the OTP (replace with SMS in production)
            import logging
            logger = logging.getLogger(__name__)
            logger.info(f"Mobile OTP for user {user_id}: {mobile_otp}")
            send_sms_otp(profile.mobile, mobile_otp)

            messages.success(request, 'Email verified. Verification code sent to your mobile.')
            context = {
                "show_mobile_otp": True
            }
            context.update(_signup_session_context())
            return render(request, "public/index.html", context)
        
        # Mobile OTP verification step
        if entered_mobile_otp:
            otp_valid, otp_error = validate_otp(entered_mobile_otp)
            if not otp_valid:
                context = {
                    "error": otp_error,
                    "show_mobile_otp": True
                }
                context.update(_signup_session_context())
                return render(request, "public/index.html", context)

            user_id = request.session.get('otp_user_id')
            if not user_id:
                return redirect("index")

            try:
                profile = UserProfile.objects.get(user_id=user_id)
            except UserProfile.DoesNotExist:
                return redirect("index")

            # Check OTP expiry (10 minutes)
            if timezone.now() > profile.mobile_otp_created_at + timedelta(minutes=10):
                context = {
                    "error": "OTP expired. Please request a new one.",
                    "show_mobile_otp": True
                }
                context.update(_signup_session_context())
                return render(request, "public/index.html", context)

            # Verify mobile OTP
            if entered_mobile_otp != profile.mobile_otp:
                context = {
                    "error": "Invalid Mobile OTP",
                    "show_mobile_otp": True
                }
                context.update(_signup_session_context())
                return render(request, "public/index.html", context)

            # Complete registration
            profile.mobile_verified = True
            profile.mobile_otp = None
            profile.mobile_otp_created_at = None
            profile.save()

            profile.user.is_active = True
            profile.user.save()

            for key in ["signup_username", "signup_name", "signup_email", "signup_mobile"]:
                request.session.pop(key, None)

            messages.success(request, 'Registration completed successfully! Please login.')
            return render(request, "public/index.html", {
                "registration_complete": True
            })

    return redirect('index')


def logout_view(request):
    logout(request)
    return redirect('index')


def test_email_view(request):
    """Test email configuration - REMOVE IN PRODUCTION"""
    from django.http import JsonResponse
    from django.core.mail import send_mail
    from django.conf import settings
    
    test_email = request.GET.get('email', 'swadhasri607@gmail.com')
    
    try:
        result = send_mail(
            'Test Email from Government Portal',
            'This is a test email to verify OTP functionality is working.',
            settings.EMAIL_HOST_USER,
            [test_email],
            fail_silently=False
        )
        
        if result == 1:
            return JsonResponse({
                'status': 'success',
                'message': f'Test email sent successfully to {test_email}',
                'email_config': {
                    'EMAIL_HOST': settings.EMAIL_HOST,
                    'EMAIL_PORT': settings.EMAIL_PORT,
                    'EMAIL_USE_TLS': settings.EMAIL_USE_TLS,
                    'EMAIL_HOST_USER': settings.EMAIL_HOST_USER
                }
            })
        else:
            return JsonResponse({
                'status': 'error',
                'message': 'Email send returned 0 - check server logs'
            })
            
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': f'Email configuration error: {str(e)}',
            'email_config': {
                'EMAIL_HOST': settings.EMAIL_HOST,
                'EMAIL_PORT': settings.EMAIL_PORT,
                'EMAIL_USE_TLS': settings.EMAIL_USE_TLS,
                'EMAIL_HOST_USER': settings.EMAIL_HOST_USER
            }
        })

