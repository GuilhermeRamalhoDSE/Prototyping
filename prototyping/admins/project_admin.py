from django.contrib import admin
from django import forms
from prototyping.models.project_models import Project
from prototyping.models.user_models import User

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