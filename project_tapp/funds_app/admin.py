from django.contrib import admin

# Register your models here.
from funds_app.models import Funds


@admin.register(Funds)
class FundsAdmin(admin.ModelAdmin):
    pass