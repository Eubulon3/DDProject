from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models
from .models import Record, Tag, Like

class RecordAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }

admin.site.register(Record, RecordAdmin)
admin.site.register(Tag)
admin.site.register(Like)