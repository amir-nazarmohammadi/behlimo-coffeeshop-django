from django.contrib import admin
from .models import Menu

class MenuAdmin(admin.ModelAdmin):
    list_display = ('titel', 'slug', 'price', 'category', 'image_tag', 'is_available')
    list_editable = ('price', 'is_available')
    

# Register your models here.
admin.site.register(Menu,MenuAdmin)
