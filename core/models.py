from django.db import models

# Create your models here.

class Item(models.Model):
    item = models.CharField(max_length=20)
    status = models.CharField(max_length=20, default="pending")

    def __str__(self):
        return self.item
