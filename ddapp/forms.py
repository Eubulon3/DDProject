from django import forms
from .models import Record

class PostRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ("title", "content",)
        widgets = {
            'content': forms.Textarea(attrs={'class': 'tinymce', 'rows': 30}),
        }

