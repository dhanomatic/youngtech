from django.contrib import admin
from .models import HouseModel

# Register your models here.

class HouseAdmin(admin.ModelAdmin):
    list_display = ('housename','housenumber')
    search_fields = ('housename','housenumber')

admin.site.register(HouseModel,HouseAdmin)