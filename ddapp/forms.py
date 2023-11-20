from django import forms
from .models import Record, Tag
from tinymce.widgets import TinyMCE
from betterforms.multiform import MultiModelForm

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

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ("tag_01", "tag_02", "tag_03", "tag_04",)
        widgets = {
            "tag_01": forms.Textarea(attrs={
                "class": "tag"
            }),
            "tag_02": forms.Textarea(attrs={
                "class": "tag"
            }),
            "tag_03": forms.Textarea(attrs={
                "class": "tag"
            }),
            "tag_04": forms.Textarea(attrs={
                "class": "tag"
            }),
        }


class RecordAndTagForm(MultiModelForm):
    form_classes = {
        "record_form": PostRecordForm,
        "tag_form": TagForm,
    }
