from django.contrib import admin
from .models import Item, Review
# Register your models here.

class ReviewInline(admin.TabularInline):
    model = Review

class ItemAdmin (admin.ModelAdmin):
    inlines = [
        ReviewInline,
    ]
    list_display = ("label", "price",)

admin.site.register(Item, ItemAdmin)
