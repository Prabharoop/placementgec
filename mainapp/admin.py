from django.contrib import admin
from .models import Placement
# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','course','reg','gender','number','branch','grad', 'desig','org', 'domain', 'degree', 'custatus', 'univname','texta','choicea','textb','textc','choiceb','choicec','textd','texte','textf','textg')
    list_filter = ('name','branch')
    search_fields = ('name','branch')

admin.site.register(Placement,AuthorAdmin)
