from django.contrib import admin

from .models import Game, SteamProfile
# Register your models here.
admin.site.register(Game)
admin.site.register(SteamProfile)