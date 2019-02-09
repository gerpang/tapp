from django.contrib import admin

# Register your models here.
from timesheet_app.models import Timesheet, Project


@admin.register(Timesheet)
class TimeSheetAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'project',
        'time_start',
        'time_end',
    )
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass
