from datetime import datetime
from uuid import UUID, uuid4
from django.db.models.query import QuerySet
from django.http import Http404, HttpRequest, HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from .models import Item


class IndexView(generic.ListView):
    template_name = "main/index.html"
    context_object_name = "latest_todo_items"

    def get_queryset(self) -> QuerySet[Item]:
        return Item.objects.order_by("-due")


class DetailView(generic.DetailView):
    slug_url_kwarg = "uuid"
    slug_field = "uuid"
    model = Item
    template_name = "main/detail.html"


def add(request: HttpRequest) -> HttpResponse:
    item = Item()
    item.uuid = uuid4()
    item.title = request.POST["title"]
    item.due = datetime.strptime(request.POST["datetime"], "%Y-%m-%d %H:%M")
    item.save()
    return HttpResponseRedirect(reverse("main:index"))
