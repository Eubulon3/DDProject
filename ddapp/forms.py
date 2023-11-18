from django import forms
from .models import Record
from tinymce.widgets import TinyMCE

class PostRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ("title", "content",)
        widgets = {
            "content": TinyMCE(attrs={
                "cols": 200,
                "rows": 40
            })
        }

