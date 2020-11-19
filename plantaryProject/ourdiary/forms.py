from .models import Ourdiary, Comment
from django import forms

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)

#class CommentForm(forms.ModelForm):
#    class Meta:
#        model = Comment
#        fields = ['content']
#        widgets = {
#            'content':forms.TextInput(attrs = {'placeholder':'댓글을 작성하세요.'})
#        }