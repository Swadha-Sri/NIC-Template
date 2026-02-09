"""Profile management views"""
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProfileEditForm, ChangePasswordForm
from django.contrib.auth import logout


@login_required(login_url='login')
def profile_view(request):
    """Display user profile page"""
    user = request.user
    profile = user.userprofile
    login_history = user.login_history.all()[:10]  # Last 10 logins
    
    context = {
        'user': user,
        'profile': profile,
        'login_history': login_history
    }
    return render(request, 'accounts/profile.html', context)


@login_required(login_url='login')
def edit_profile_view(request):
    """Edit user profile details"""
    user = request.user
    profile = user.userprofile
    
    if request.method == 'POST':
        form = ProfileEditForm(request.POST)
        if form.is_valid():
            # Update user
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data.get('last_name', '')
            user.email = form.cleaned_data['email']
            user.save()
            
            # Update profile
            profile.mobile = form.cleaned_data['mobile']
            profile.save()
            
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
        else:
            context = {
                'form': form,
                'errors': form.errors
            }
            return render(request, 'accounts/edit_profile.html', context)
    else:
        form = ProfileEditForm(initial={
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'mobile': profile.mobile
        })
    
    context = {'form': form}
    return render(request, 'accounts/edit_profile.html', context)


@login_required(login_url='login')
def change_password_view(request):
    """Change user password"""
    user = request.user
    
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            old_password = form.cleaned_data['old_password']
            new_password = form.cleaned_data['new_password']
            
            # Verify old password
            if not user.check_password(old_password):
                form.add_error('old_password', 'Current password is incorrect')
                context = {'form': form}
                return render(request, 'accounts/change_password.html', context)
            
            # Set new password
            user.set_password(new_password)
            user.save()
            
            messages.success(request, 'Password changed successfully! Please login again.')
            logout(request)
            return redirect('login')
        else:
            context = {
                'form': form,
                'errors': form.errors
            }
            return render(request, 'accounts/change_password.html', context)
    else:
        form = ChangePasswordForm()
    
    context = {'form': form}
    return render(request, 'accounts/change_password.html', context)
