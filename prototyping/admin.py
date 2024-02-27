from django.contrib import admin
from prototyping.models.license_models import License
from prototyping.models.user_models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


admin.site.register(License)

class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ('email', 'first_name', 'last_name', 'license', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'license')}),
        ('Permissions', {'fields': ('is_active', 'is_staff',                        'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'license')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(User, UserAdmin)