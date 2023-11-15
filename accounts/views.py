from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth import login
from .forms import CustomUserCreationForm


class LoginView(LoginView):
    firlds = "__all__"
    template_name = "login.html"

    def get_success_url(self):
        return reverse_lazy("ddapp:index")


class SignupView(generic.FormView):
    template_name = "signup.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("ddapp:index")

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)



