from django.contrib import admin
from prototyping.models.notification_models import Notification

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('message', 'user', 'is_read', 'displayed_date')
    list_filter = ('is_read', 'user')
    search_fields = ('message__message', 'user__username')
    date_hierarchy = 'message__date'

    def displayed_date(self, obj):
        return obj.message.date.strftime("%Y-%m-%d %H:%M:%S")
    displayed_date.admin_order_field = 'message__date'
    displayed_date.short_description = 'Date of Message'

admin.site.register(Notification, NotificationAdmin)
