from django.db import models

# Create your models here.

class Game(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.URLField()
    description = models.TextField()
    updated_at = models.DateTimeField(auto_now_add=True)