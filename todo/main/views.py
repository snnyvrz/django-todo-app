from datetime import datetime
from uuid import UUID, uuid4
from django.http import Http404, HttpRequest, HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.urls import reverse

from .models import Item


def index(request: HttpRequest) -> HttpResponse:
    latest_todo_items = Item.objects.order_by("-due")
    template = loader.get_template("main/index.html")
    context = {"latest_todo_items": latest_todo_items}
    return HttpResponse(template.render(context, request))


def detail(request: HttpRequest, uuid: UUID) -> HttpResponse:
    try:
        item = Item.objects.get(uuid=uuid)
    except Item.DoesNotExist:
        raise Http404("Item does not exist.")
    return render(request, "main/detail.html", {"item": item})


def add(request: HttpRequest) -> HttpResponse:
    item = Item()
    item.uuid = uuid4()
    item.title = request.POST["title"]
    item.due = datetime.strptime(request.POST["datetime"], "%Y-%m-%d %H:%M")
    item.save()
    return HttpResponseRedirect(reverse("main:index"))
