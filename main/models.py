import uuid
from django.db import models

# Create your models here.
class Product(models.Model):
    CATEGORY_CHOICES = [
        ('bola basket', 'Bola Basket'),
        ('bola tenis', 'Bola Tenis'),
        ('bola ping-pong', 'Bola Ping-pong'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField()
    is_featured = models.BooleanField()

    def __str__(self):
        return self.id