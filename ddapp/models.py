from django.db import models
from tinymce.models import HTMLField
from django.conf import settings



class Record(models.Model):
    title = models.CharField(max_length=100, verbose_name="タイトル")
    content = HTMLField(verbose_name="内容")
    user_record = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="ユーザー")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日")

    def __str__(self):
        return self.title


class Tag(models.Model):
    tag_01 = models.CharField(max_length=20, verbose_name="タグ01", null=True, blank=True)
    tag_02 = models.CharField(max_length=20, verbose_name="タグ02", null=True, blank=True)
    tag_03 = models.CharField(max_length=20, verbose_name="タグ03", null=True, blank=True)
    tag_04 = models.CharField(max_length=20, verbose_name="タグ04", null=True, blank=True)
    tag_record = models.ForeignKey(Record, on_delete=models.CASCADE, verbose_name = "レコード", null=True, blank=True)

    def __str__(self):
        return str(self.tag_record)
