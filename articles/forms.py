from django import forms
from .models import Commentary

class CommentaryFrom(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ['content']