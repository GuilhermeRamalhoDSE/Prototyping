# admin.py
from django.contrib import admin
from prototyping.models.component_release_models import ComponentRelease
from prototyping.models.release_models import Release

@admin.register(ComponentRelease)
class ComponentReleaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'release', 'chassis', 'element', 'component', 'file')
    search_fields = ('release__name', 'chassis__name', 'element__name', 'component__name')
    list_filter = ('release', 'chassis', 'element', 'component')

    def get_queryset(self, request):

        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs

        return qs.filter(release__project__client=request.user.client)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "release" and not request.user.is_superuser:
            kwargs["queryset"] = Release.objects.filter(project__client=request.user.client)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
