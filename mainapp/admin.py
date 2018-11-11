from django.contrib import admin
from .models import Placement
# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','course','number','branch','grad', 'desig','org')
    list_filter = ('name','branch')
    search_fields = ('name','branch')

admin.site.register(Placement,AuthorAdmin)
