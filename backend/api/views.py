from django.shortcuts import render
from api.models import Game
from api.serializers import GameSerializer
from rest_framework import generics

# Create your views here.
class GameListCreate(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer