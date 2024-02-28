from django.contrib import admin
from prototyping.models.license_models import License
from prototyping.models.user_models import User
from prototyping.models.chassis_models import Chassis
from prototyping.models.aptica_models import Aptica
from prototyping.models.element_models import Element
from prototyping.models.component_model import Component
from prototyping.models.client_models import Client
from prototyping.models.project_models import Project
from prototyping.models.message_models import Message
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django import forms
from django.db.models import Q
from django.utils.translation import gettext_lazy as _


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
    list_display = ('id', 'name', 'creation_date', 'last_modified_date', 'file', 'license')
    search_fields = ('name',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(license=request.user.license)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "license" and not request.user.is_superuser:
            kwargs["queryset"] = License.objects.filter(id=request.user.license.id)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
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

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "chassis":
            if not request.user.is_superuser:
                kwargs["queryset"] = Chassis.objects.filter(license=request.user.license)
            else:
                kwargs["queryset"] = Chassis.objects.all()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    

@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'version_id', 'element', 'name', 'position_x', 'position_y', 'position_z',
        'rotation_x', 'rotation_y', 'rotation_z', 'rotation_w',
        'area_radius', 'haptic_stiffness', 'haptic_temperature', 'haptic_texture', 'file', 'created_at'
    )
    search_fields = ('name', 'element__name') 
    list_filter = ('version_id', 'element', 'created_at')  
    fields = (
        'version_id', 'element', 'name', 'position_x', 'limit_position_x', 'position_y', 'limit_position_y',
        'position_z', 'limit_position_z', 'rotation_x', 'limit_rotation_x',
        'rotation_y', 'limit_rotation_y', 'rotation_z', 'limit_rotation_z',
        'rotation_w', 'limit_rotation_w', 'area_radius', 'haptic_stiffness',
        'haptic_temperature', 'haptic_texture', 'file', 'created_at'
    )
    readonly_fields = ('created_at',)  

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

class ProjectAdminForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    form = ProjectAdminForm
    list_display = ['id', 'name', 'client', 'creation_date', 'last_release_date']
    search_fields = ['name', 'client__name']
    filter_horizontal = ['users']

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "users":
            if not request.user.is_superuser:
                license_id = request.user.license.id
                kwargs["queryset"] = User.objects.filter(license=license_id)
            else:
                kwargs["queryset"] = User.objects.all()
        return super().formfield_for_manytomany(db_field, request, **kwargs)
    
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'client', 'project', 'user', 'date', 'message']
    search_fields = ['message', 'user__email', 'client__name', 'project__name']
    list_filter = ['date', 'client', 'project']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(Q(user__license=request.user.license) | Q(client__license=request.user.license) | Q(project__client__license=request.user.license))

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "client" and not request.user.is_superuser:
            kwargs["queryset"] = Client.objects.filter(license=request.user.license)
        elif db_field.name == "project" and not request.user.is_superuser:
            kwargs["queryset"] = Project.objects.filter(client__license=request.user.license)
        elif db_field.name == "user" and not request.user.is_superuser:
            kwargs["queryset"] = User.objects.filter(license=request.user.license)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)