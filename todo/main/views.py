from django.http import Http404, HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import Item


def index(request):
    latest_todo_items = Item.objects.order_by("-due")
    template = loader.get_template("main/index.html")
    context = {"latest_todo_items": latest_todo_items}
    return HttpResponse(template.render(context, request))


def detail(request, uuid):
    try:
        item = Item.objects.get(uuid=uuid)
    except Item.DoesNotExist:
        raise Http404("Item does not exist.")
    return render(request, "main/detail.html", {"item": item})
