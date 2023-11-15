from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView

app_name = "accounts"
urlpatterns = [
    path("login/", views.LoginView.as_view(), name = "login"),
    path("signup/", views.SignupView.as_view(), name = "signup"),
    path("logout/", LogoutView.as_view(next_page = "accounts:login"), name = "logout")
]
