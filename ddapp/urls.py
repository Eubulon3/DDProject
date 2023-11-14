from django.urls import path, include
from . import views

app_name = "ddapp"
urlpatterns = [
    path("", views.IndexView.as_view(), name = "index"),
    path("mypage/", views.MypageView.as_view(), name = "mypage"),
]
