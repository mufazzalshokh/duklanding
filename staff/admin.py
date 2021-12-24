from django.contrib import admin

from staff.models import StaffModel


@admin.register(StaffModel)
class StaffModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name']
