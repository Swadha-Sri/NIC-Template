from django.urls import path
from . import views
from .profile_views import profile_view, edit_profile_view, change_password_view

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('test-email/', views.test_email_view, name='test_email'),  # For debugging only
    path('profile/', profile_view, name='profile'),
    path('profile/edit/', edit_profile_view, name='edit_profile'),
    path('profile/change-password/', change_password_view, name='change_password'),
]
