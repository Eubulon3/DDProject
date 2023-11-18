from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Record
from .forms import PostRecordForm

class IndexView(LoginRequiredMixin, generic.TemplateView):
    template_name = "index.html"


class MypageView(LoginRequiredMixin, generic.TemplateView):
    template_name = "mypage.html"

class PostRecordView(LoginRequiredMixin, generic.CreateView):
    model = Record
    template_name = "postrecord.html"
    form_class = PostRecordForm
    success_url = reverse_lazy("ddapp:index")

    def form_valid(self, form):
        record = form.save(commit=False)
        record.user_record = self.request.user
        record.save()
        messages.success(self.request, "post成功しました")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "postに失敗しました")
        return super().form_invalid(form)
    
    