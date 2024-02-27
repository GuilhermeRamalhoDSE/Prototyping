from django.contrib import admin
from prototyping.models.license_models import License
from prototyping.models.user_models import User
from prototyping.models.chassis_models import Chassis
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType


@admin.register(License)
class LicenseAdmin(admin.ModelAdmin):
    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_add_permission(self, request):
        return request.user.is_superuser


class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ('email', 'first_name', 'last_name', 'license', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'license')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'license')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(license=request.user.license)

    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser:
            obj.license = request.user.license
        super().save_model(request, obj, form, change)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "license" and not request.user.is_superuser:
            kwargs["queryset"] = License.objects.filter(id=request.user.license.id)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "user_permissions" and not request.user.is_superuser:
            user_content_type = ContentType.objects.get_for_model(User)
            kwargs["queryset"] = Permission.objects.filter(content_type=user_content_type)
        return super().formfield_for_manytomany(db_field, request, **kwargs)

admin.site.register(User, UserAdmin)

@admin.register(Chassis)
class ChassisAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'creation_date', 'last_modified_date', 'file')
    search_fields = ('name',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(license=request.user.license)