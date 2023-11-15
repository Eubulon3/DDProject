from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):

  class Meta:
    model = get_user_model()
    fields = ["username",] #passwordは別の場所に処理があるらしい
    labels = {
      "username": "ユーザー名",
    }
    help_texts = {
      "username": "",
    }
