from django.contrib import admin
from django.utils.html import format_html
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'mobile', 'email_verified_badge', 'mobile_verified_badge', 'created_at')
    list_filter = ('email_verified', 'mobile_verified', 'created_at')
    search_fields = ('user__username', 'user__email', 'mobile')
    readonly_fields = ('created_at', 'updated_at', 'user')
    
    fieldsets = (
        ('User Information', {
            'fields': ('user',)
        }),
        ('Contact Details', {
            'fields': ('mobile',)
        }),
        ('Email Verification', {
            'fields': ('email_verified', 'email_otp', 'email_otp_created_at')
        }),
        ('Mobile Verification', {
            'fields': ('mobile_verified', 'mobile_otp', 'mobile_otp_created_at')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def username(self, obj):
        return obj.user.username
    username.short_description = 'Username'

    def email_verified_badge(self, obj):
        if obj.email_verified:
            return format_html('<span style="color: green;">✓ Verified</span>')
        return format_html('<span style="color: red;">✗ Not Verified</span>')
    email_verified_badge.short_description = 'Email Status'

    def mobile_verified_badge(self, obj):
        if obj.mobile_verified:
            return format_html('<span style="color: green;">✓ Verified</span>')
        return format_html('<span style="color: red;">✗ Not Verified</span>')
    mobile_verified_badge.short_description = 'Mobile Status'

