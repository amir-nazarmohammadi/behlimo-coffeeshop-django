from django.contrib import admin
from .models import Comment
# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display = ['full_name' , 'email' ,'menu','comment_time', 'message', 'is_active' ]
    list_editable = ('is_active',)
    list_filter = ['menu' , 'time']
    search_fields = ['email','full_name','messeage']
admin.site.register(Comment,CommentAdmin)