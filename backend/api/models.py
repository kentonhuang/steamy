from django.db import models
from django.contrib.postgres.fields import ArrayField, JSONField

# Create your models here.

class Game(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=100)
    dev = ArrayField(models.CharField(max_length=100))
    pub = ArrayField(models.CharField(max_length=100))
    name = models.CharField(max_length=100)
    price = JSONField()
    previous_price = JSONField()
    image = models.URLField()
    description = models.TextField(blank=True)
    short_desc = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    dlc = ArrayField(models.IntegerField(), blank=True)
    genres = ArrayField(JSONField(), blank=True)
    platforms = JSONField(blank=True)
    release_date = JSONField()