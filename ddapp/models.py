from django.db import models
from tinymce.models import HTMLField
from django.conf import settings

class Record(models.Model):
    title = models.CharField(max_length=100, verbose_name="タイトル")
    # tags_record = models.OneToOneField(vervose_name = "タグ")
    content = HTMLField(verbose_name="内容")
    user_record = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="ユーザー")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日")



