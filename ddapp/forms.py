from django import forms
from .models import Record
from tinymce.widgets import TinyMCE

class PostRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ("title", "content",)
        widgets = {
            "title": forms.Textarea(attrs={
                "class": "record-title",
                "cols": 20,
                "rows": 1,
            }),
            "content": TinyMCE(attrs={
                "class": "record-content",
                "cols": 200,
                "rows": 40,
            },
            )
        }

