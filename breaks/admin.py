from django.contrib import admin
from django.contrib.admin import TabularInline

from breaks.models import organizations, groups, replacements


class ReplacementEmployeeInline(TabularInline):
    model = replacements.ReplacementEmployee
    fields = ('employee', 'status',)


@admin.register(organizations.Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'director')
    list_display_links = ('id', 'name')


@admin.register(groups.Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'manager', 'min_active')
    list_display_links = ('id', 'name')


@admin.register(replacements.Replacement)
class ReplacementAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'group', 'break_start')
    list_display_links = ('id', 'date', 'group')

    inlines = (
        ReplacementEmployeeInline,
    )

@admin.register(replacements.ReplacementStatus)
class ReplacementStatusAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'is_active')
    list_display_links = ('name', 'code')

