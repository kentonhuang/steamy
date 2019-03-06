from rest_framework import serializers
from api.models import Game, SteamProfile, TestModel, ShortProfile

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'

class SteamProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SteamProfile
        fields = '__all__'

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestModel
        fields = '__all__'

class ShortProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortProfile
        fields = '__all__'