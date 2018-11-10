from django.contrib import admin
from .models import Placement
# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'email', 'course' , 'branch' , 'org', 'domain' , 'desig')
    list_filter = ('name','branch')
    search_fields = ('name','branch')

admin.site.register(Placement,AuthorAdmin)
