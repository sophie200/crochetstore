from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Item

class ItemListView(ListView):
    model = Item
    context_object_name = 'item_list'
    template_name = 'items/item_list.html'


class ItemDetailView(DetailView):
    model = Item
    context_object_name = 'item'
    template_name = 'items/item_detail.html'
