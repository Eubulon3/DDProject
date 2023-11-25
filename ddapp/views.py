from typing import Any
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q
from django.conf import settings
from .models import Record, Tag, Like
from .forms import RecordAndTagForm


def like_view(request):
    record_id = request.POST.get("record_id")
    context = {
        "user": f"request.user",
    }
    record = get_object_or_404(Record, id=record_id)
    like = Like.objects.filter(like_from_user = request.user, like_record = record)
    to_user = record.user_record

    if like.exists():
        like.delete()
        context["method"] = "delete"
    else:
        like.create(like_record = record, like_from_user = request.user, like_to_user = to_user)
        context["method"] = "create"
    
    context["like_count"] = record.like_set.count()

    return JsonResponse(context)



class IndexView(LoginRequiredMixin, generic.ListView):
    model = Record
    template_name = "index.html"
    context_object_name = "records"

    def get_queryset(self):
        records = Record.objects.filter(user_record = self.request.user).order_by("created_at")
        search = self.request.GET.get("search")

        if search:
            records = records.filter(
                Q(title__icontains=search) | Q(content__icontains=search)
            )

        return records
    


class MypageView(LoginRequiredMixin, generic.TemplateView):
    template_name = "mypage.html"
    model = settings.AUTH_USER_MODEL

    def calc_rank(self, count):
        rank = ["A", "B", "C", "D", "E"]

        if 0 < count <= 3:
            n = 4
        elif 3 < count <= 12:
            n = 3
        elif 12 < count <= 36:
            n = 2
        elif 36 < count <= 96:
            n = 1
        else:
            n = 0

        return rank[n]
        

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["user"] = user
        my_rank = self.calc_rank(user.record_set.count())
        context = {
            "record_count": user.record_set.count(),
            "like_count": Like.objects.filter(like_to_user = user).count(),
            "rank": my_rank,
        }
        return context



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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        like_count = self.object.like_set.count()

        context["like_count"] = like_count

        if self.object.like_set.filter(like_from_user = self.request.user).exists():
            context["like"] = True
        else:
            context["like"] = False

        return context


class SearchRecordView(LoginRequiredMixin, generic.ListView):
    model = Record
    template_name = "search.html"
    context_object_name = "records"

    def get_queryset(self):
        records = Record.objects.all().order_by("created_at")
        search = self.request.GET.get("search")

        if search:
            records = records.filter(
                Q(title__icontains=search) | Q(content__icontains=search)
            )

        return records
    
class LikeListView(LoginRequiredMixin, generic.ListView):
    model = Like
    template_name = "like_list.html"

    def queryset(self):
        like_records = Like.objects.filter(like_from_user = self.request.user)
        return like_records

