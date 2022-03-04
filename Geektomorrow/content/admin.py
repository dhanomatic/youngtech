from django.contrib import admin
from .models import ContentModel,UserModel

# Register your models here.

class ContentAdmin(admin.ModelAdmin):
    list_display = ('username','title','content')
    search_fields = ('username','title','content')


class UserAdmin(admin.ModelAdmin):
    list_display = ('domain','city','country')
    search_fields = ('domain','city','country')


admin.site.register(UserModel,UserAdmin)
admin.site.register(ContentModel,ContentAdmin)
