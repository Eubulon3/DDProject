from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Record, Tag
from .forms import RecordAndTagForm

class IndexView(LoginRequiredMixin, generic.ListView):
    model = Record
    template_name = "index.html"
    context_object_name = "records"

    def get_queryseet(self):
        records = Record.objects.filter(user_record = self.request.user).order_by("-created_at")
        return records


class MypageView(LoginRequiredMixin, generic.TemplateView):
    template_name = "mypage.html"

class PostRecordView(LoginRequiredMixin, generic.CreateView):
    model = Record
    template_name = "postrecord.html"
    form_class = RecordAndTagForm
    success_url = reverse_lazy("ddapp:index")

    def form_valid(self, form):
        record = form["record_form"].save(commit=False)
        record.user_record = self.request.user
        record.save()

        tag = form["tag_form"].save(commit=False)
        tag.tag_record = record
        tag.save()
        messages.success(self.request, "post成功しました")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "postに失敗しました")
        return super().form_invalid(form)

class DetailRecordView(LoginRequiredMixin, generic.DetailView):
    model = Record
    template_name = "detail.html"
    pk_url_kwarg = "id"