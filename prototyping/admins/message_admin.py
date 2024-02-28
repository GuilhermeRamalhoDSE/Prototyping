from django.contrib import admin
from prototyping.models.message_models import Message
from prototyping.models.client_models import Client
from prototyping.models.project_models import Project
from prototyping.models.user_models import User
from django.db.models import Q

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