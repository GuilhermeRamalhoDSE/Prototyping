from django.contrib import admin
from prototyping.models.aptica_models import Aptica
from prototyping.models.license_models import License


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