from django.contrib import admin
from prototyping.models.release_models import Release

@admin.register(Release)
class ReleaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'client_id', 'project_id', 'name', 'file', 'creation_date')
    search_fields = ('name', 'client_id__name', 'project_id__name')  
    list_filter = ('client_id', 'project_id', 'creation_date')
    date_hierarchy = 'creation_date'  

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs 
        return qs.filter(client_id=request.user.client_id)