from django.db import models
from django.contrib.postgres.fields import ArrayField, JSONField

# Create your models here.

class Game(models.Model):
    id = models.IntegerField(primary_key=True)
    game_type = models.CharField(max_length=500)
    dev = ArrayField(models.CharField(max_length=500), blank=True, null=True)
    pub = ArrayField(models.CharField(max_length=500), blank=True, null=True)
    name = models.CharField(max_length=500)
    price = JSONField(blank=True, null=True)
    previous_price = JSONField(blank=True, null=True)
    image = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True)
    short_desc = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    dlc = ArrayField(models.IntegerField(), blank=True, null=True)
    genres = JSONField(default=list)
    platforms = JSONField(blank=True, null=True)
    release_date = JSONField(blank=True, null=True)

    def __str__(self):
        return self.name + ' ' + str(id)

class SteamProfile(models.Model):
    id64 = models.BigIntegerField(primary_key=True)
    vanity_url = models.CharField(max_length=500, blank=True)
    steam_url = models.URLField(blank=True, null=True)
    visibility = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=500, blank=True)
    real_name = models.CharField(max_length=500, blank=True)
    profile_state = models.IntegerField(blank=True, null=True)
    primary_clan = models.BigIntegerField(blank=True, null=True)
    loc_country = models.CharField(max_length=10, blank=True, null=True)
    loc_state = models.CharField(max_length=10, blank=True, null=True)
    loc_city = models.IntegerField(blank=True, null=True)
    in_game = models.IntegerField(blank=True, null=True)
    in_game_name = models.CharField(max_length=500, blank=True,)
    status = models.IntegerField(blank=True, null=True)
    avatar = models.URLField(blank=True, null=True)
    avatar_med = models.URLField(blank=True, null=True)
    avatar_full = models.URLField(blank=True, null=True)
    games_owned = JSONField(blank=True, null=True)
    recent_games = JSONField(blank=True, null=True)
    friends = JSONField(blank=True, null=True)
    level = models.IntegerField(blank=True,null=True)
    bans= JSONField(default=list)
    badges = JSONField(blank=True,null=True)
    last_online = models.IntegerField(blank=True, null=True)
    time_created = models.IntegerField(blank=True, null=True)
    last_updated = models.DateTimeField(auto_now_add=True)

class TestModel(models.Model):
    name=models.CharField(max_length=500, blank=True)


