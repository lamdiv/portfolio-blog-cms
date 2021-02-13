from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Name'}),label='')
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'comment-gap','rows':'5','placeholder':'Your Comment'}),label='')
    
    class Meta:
        model = Comment
        fields = ('name', 'body')

