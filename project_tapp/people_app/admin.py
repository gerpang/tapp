from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from people_app.models import User, Cluster, Institution

admin.site.register(User, UserAdmin)


@admin.register(Cluster)
class ClusterAdmin(admin.ModelAdmin):
    pass


@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    pass
