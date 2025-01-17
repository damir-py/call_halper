from django.contrib import admin
from django.contrib.admin import TabularInline

from breaks.models import organizations, groups, replacements, dicts, breaks


######################
# IN LINES
######################
class ReplacementEmployeeInline(TabularInline):
    model = replacements.ReplacementEmployee
    fields = ('employee', 'status',)


######################
# MODEL ADMIN
######################
@admin.register(organizations.Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'director')
    list_display_links = ('id', 'name')

    filter_horizontal = ('employee',)


@admin.register(groups.Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'manager', 'min_active')
    list_display_links = ('id', 'name')

    search_fields = ('name',)


@admin.register(replacements.Replacement)
class ReplacementAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'group', 'break_start')
    list_display_links = ('id', 'date', 'group')

    autocomplete_fields =('group',)

    inlines = (
        ReplacementEmployeeInline,
    )


@admin.register(dicts.ReplacementStatus)
class ReplacementStatusAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'sort', 'is_active')
    list_display_links = ('name', 'code')


@admin.register(dicts.BreakStatus)
class BreakStatusAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'sort', 'is_active')
    list_display_links = ('name', 'code')


@admin.register(breaks.Break)
class BreakAdmin(admin.ModelAdmin):
    list_display = ('id', 'replacement', 'break_start', 'break_end',)
    list_display_links = ('id', 'replacement',)
    list_filter = ('status',)
