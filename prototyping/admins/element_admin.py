from django.contrib import admin
from prototyping.models.element_models import Element
from prototyping.models.chassis_models import Chassis


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