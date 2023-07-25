from django.contrib import admin
from .models import Table
# Register your models here.
class TabelAdmin(admin.ModelAdmin):
    list_display= ('name', 'is_reserved')
    list_editable = ('is_reserved',)

# Register your models here.
admin.site.register(Table,TabelAdmin)