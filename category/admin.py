from django.contrib import admin
from .models import Category



# Register your models here

class CategoryAdmin(admin.ModelAdmin):
    list_display= ('titel','slug','image_tag')


admin.site.register(Category,CategoryAdmin)
