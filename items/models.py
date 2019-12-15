import uuid
from django.db import models
from django.urls import reverse

# Create your models here.
class Item(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    label = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.label

    def get_absolute_url(self):
        return reverse('item_detail', args=[str(self.id)])
