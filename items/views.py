from django.db.models import Q
from django.shortcuts import render
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin
)
from django.views.generic import ListView, DetailView

from .models import Item

class ItemListView(LoginRequiredMixin, ListView):
    model = Item
    context_object_name = 'item_list'
    template_name = 'items/item_list.html'
    login_url = 'account_login'


class ItemDetailView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    DetailView):
    model = Item
    context_object_name = 'item'
    template_name = 'items/item_detail.html'
    login_url = 'account_login'
    permission_required = 'items.special_status'

class SearchResultsListView(ListView):
    model = Item
    context_object_name = 'item_list'
    template_name = 'items/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Item.objects.filter(
            Q(label__icontains=query) | Q(price__icontains=query)
            )
