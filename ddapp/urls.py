from django.urls import path, include
from . import views

app_name = "ddapp"
urlpatterns = [
    path("", views.IndexView.as_view(), name = "index"),
    path("accounts/", include("accounts.urls")),
    path("mypage/", views.MypageView.as_view(), name = "mypage"),
    path("post/", views.PostRecordView.as_view(), name = "post"),
    path("detailrecord/<int:id>/", views.DetailRecordView.as_view(), name = "detail")
]
