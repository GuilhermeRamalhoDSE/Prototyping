from django.contrib import admin
from prototyping.models.license_models import License
from prototyping.models.user_models import User
from prototyping.models.chassis_models import Chassis
from prototyping.models.aptica_models import Aptica
from prototyping.models.element_models import Element
from prototyping.models.component_model import Component
from prototyping.models.client_models import Client
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
    
@admin.register(Aptica)
class ApticaAdmin(admin.ModelAdmin):
    list_display = ('id', 'license', 'hand', 'mac_address')
    search_fields = ('mac_address',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(license=request.user.license.id)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "license" and not request.user.is_superuser:
            kwargs["queryset"] = License.objects.filter(id=request.user.license.id)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

@admin.register(Element)
class ElementAdmin(admin.ModelAdmin):
    list_display = ('id', 'chassis', 'name', 'component_count')
    search_fields = ('name',)
    list_filter = ('chassis',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(chassis__license=request.user.license)
    
@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'version_id', 'name', 'position_x', 'position_y', 'position_z',
        'rotation_x', 'rotation_y', 'rotation_z', 'rotation_w',
        'area_radius', 'haptic_stiffness', 'haptic_temperature', 'haptic_texture'
    )
    search_fields = ('name',)
    list_filter = ('version_id',)
    fields = (
        'version_id', 'name', 'position_x', 'limit_position_x', 'position_y', 'limit_position_y',
        'position_z', 'limit_position_z', 'rotation_x', 'limit_rotation_x',
        'rotation_y', 'limit_rotation_y', 'rotation_z', 'limit_rotation_z',
        'rotation_w', 'limit_rotation_w', 'area_radius', 'haptic_stiffness',
        'haptic_temperature', 'haptic_texture'
    )

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'address', 'phone')
    search_fields = ('name', 'email')
    list_filter = ('name', 'email')

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