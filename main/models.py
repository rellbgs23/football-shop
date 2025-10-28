import uuid
from django.db import models
# ti4
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    CATEGORY_CHOICES = [
        ('bola basket', 'Bola Basket'),
        ('bola tenis', 'Bola Tenis'),
        ('bola ping-pong', 'Bola Ping-pong'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES
    )
    is_featured = models.BooleanField()

    def __str__(self):
        return self.name