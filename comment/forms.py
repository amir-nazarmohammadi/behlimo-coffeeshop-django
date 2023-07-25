from django import forms
from .models import Comment

class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = 'is_active','menu',
    
