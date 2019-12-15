from django.urls import path

from .views import ItemListView, ItemDetailView

urlpatterns = [
    path('', ItemListView.as_view(), name='item_list'),
    path('<uuid:pk>', ItemDetailView.as_view(), name='item_detail'),
]
