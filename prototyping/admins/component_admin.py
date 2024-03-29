from django.contrib import admin
from prototyping.models.component_model import Component

@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'version_id', 'element', 'name', 'limit_position_x', 'limit_position_y',
        'limit_position_z', 'limit_rotation_x', 'limit_rotation_y', 'limit_rotation_z',
        'limit_rotation_w', 'area_radius', 'haptic_stiffness', 'haptic_temperature',
        'haptic_texture', 'file', 'created_at'
    )
    search_fields = ('name', 'element__name')
    list_filter = ('version_id', 'element', 'created_at')
    fields = (
        'version_id', 'element', 'name', 'limit_position_x', 'limit_position_y',
        'limit_position_z', 'limit_rotation_x', 'limit_rotation_y', 'limit_rotation_z',
        'limit_rotation_w', 'area_radius', 'haptic_stiffness', 'haptic_temperature',
        'haptic_texture', 'file', 'created_at'
    )
    readonly_fields = ('created_at',)
