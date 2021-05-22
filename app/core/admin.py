from core import models
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext

class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = ((None, {
        'fields': ('url', 'title', 'content', 'sites')
    }),
                 ('Advanced options', {
                     'classes': ('collapse',),
                     'fields': ('registration_required', 'template_name'),
                 }),)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )


admin.site.register(models.User, UserAdmin)
