from django.contrib import admin

from .models import Profile, SocialAccount


class SocialAccountInline(admin.TabularInline):
    model = SocialAccount


class ProfileAdmin(admin.ModelAdmin):
    inlines = [SocialAccountInline, ]


admin.site.register(Profile, ProfileAdmin)
admin.site.register(SocialAccount)