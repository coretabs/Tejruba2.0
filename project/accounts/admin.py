from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from .models import Profile, SocialAccount


class SocialAccountInline(admin.TabularInline):
    model = SocialAccount


class ProfileInline(admin.TabularInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )


class ProfileAdmin(admin.ModelAdmin):
    inlines = [SocialAccountInline, ]


# admin.site.unregister(User)
# admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile, ProfileAdmin)