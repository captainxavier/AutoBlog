from django import forms
from comments.models import Comments


class CommentForm(forms.ModelForm):

    content = forms.CharField(widget=forms.Textarea(attrs={    
        'class': 'comment-form-control pointer-small',
        'placeholder': 'Comment',
        'id':'user_comment'
   }))

    class Meta:
        model = Comments
        fields = ('content',)