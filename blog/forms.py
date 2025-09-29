from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text',)      
        widgets = {
            'author': forms.TextInput(attrs={'placeholder': 'तुमचे नाव', 'class': 'form-control'}),
            'text': forms.Textarea(attrs={'placeholder': 'तुमची कमेंट...', 'class': 'form-control', 'rows': 4}),
        }

