from django.contrib import admin

from breaks.models import organizations


@admin.register(organizations.Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'director')
    list_display_links = ('id', 'name')


@admin.register(organizations.Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'manager', 'min_active', 'break_duration')
    list_display_links = ('id', 'name')
