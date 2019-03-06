from django.shortcuts import render
from api.models import Game, SteamProfile, TestModel, ShortProfile
from api.serializers import GameSerializer, SteamProfileSerializer, TestSerializer, ShortProfileSerializer
from rest_framework import generics, status
from rest_framework.response import Response

import requests
import json

# Create your views here.
class GameListCreate(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class DetailGame(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class SteamProfileList(generics.ListCreateAPIView):
    queryset = SteamProfile.objects.all()
    serializer_class = SteamProfileSerializer

class SteamProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SteamProfile.objects.all()
    serializer_class = SteamProfileSerializer

    def get(self, request, pk, *args, **kwargs):
        if SteamProfile.objects.filter(pk=self.kwargs.get('pk')).exists():
            profile = SteamProfile.objects.get(pk=self.kwargs.get('pk'))
            serializer = SteamProfileSerializer(profile)
            return Response(serializer.data)
        else:
            pkstr = str(pk)
            url_summary = 'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=8BED1F5C904666F005800A4B9A5A1162&steamids=' + pkstr
            url_friends = 'http://api.steampowered.com/ISteamUser/GetFriendList/v1/?key=8BED1F5C904666F005800A4B9A5A1162&steamid=' + pkstr
            url_games = 'http://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key=8BED1F5C904666F005800A4B9A5A1162&steamid='+ pkstr + '&include_played_free_games=1&include_appinfo=true'
            url_badges = 'http://api.steampowered.com/IPlayerService/GetBadges/v1/?key=8BED1F5C904666F005800A4B9A5A1162&steamid=' + pkstr
            url_bans = 'http://api.steampowered.com/ISteamUser/GetPlayerBans/v1/?key=8BED1F5C904666F005800A4B9A5A1162&steamids=' + pkstr
            url_recent_games = 'http://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v1/?key=8BED1F5C904666F005800A4B9A5A1162&steamid=' + pkstr
            r = requests.get(url_summary)
            data = r.json()
            user = data['response']['players']
            if not data['response']['players']:
                content = {'error': 'User does not exist'}
                return Response(content, status=status.HTTP_404_NOT_FOUND)
            elif r.status_code == 429:
                content = {'error': 'Limit reached'}
                return Response(content, status=status.HTTP_429_TOO_MANY_REQUESTS)
            else:
                keys = {
                    'id64': user[0]['steamid'],
                    'steam_url': user[0]['profileurl'],
                    'name': user[0]['personaname'],
                    'profile_state': user[0]['profilestate'],
                    'avatar': user[0]['avatar'],
                    'avatar_med': user[0]['avatarmedium'],
                    'avatar_full': user[0]['avatarfull'],
                    'status': user[0]['personastate'],
                    'last_online': user[0]['lastlogoff'],
                    'visibility': user[0]['communityvisibilitystate']
                }
                if user[0]['communityvisibilitystate'] != 1:
                    if 'realname' in user[0]:
                        keys['real_name'] = user[0]['realname']
                    if 'timecreated' in user[0]:
                        keys['time_created'] = user[0]['timecreated']
                    if 'gameid' in user[0]:
                        keys['in_game'] = user[0]['gameid']
                    if 'gameextrainfo' in user[0]:
                        keys['in_game_name'] = user[0]['gameextrainfo']
                    if 'loccountrycode' in user[0]:
                        keys['loc_country'] = user[0]['loccountrycode']
                    if 'locstatecode' in user[0]:
                        keys['loc_state'] = user[0]['locstatecode']
                    if 'loccityid' in user[0]:
                        keys['loc_city'] = user[0]['loccityid']
                    if 'primaryclanid' in user[0]:
                        keys['primary_clan'] = user[0]['primaryclanid']
                    r_friends = requests.get(url_friends)
                    r_games = requests.get(url_games)
                    r_badges = requests.get(url_badges)
                    r_bans = requests.get(url_bans)
                    r_recent_games = requests.get(url_recent_games)
                    if (r_friends.status_code == 429 or r_games.status_code == 429 or 
                    r_badges.status_code == 429 or r_bans.status_code == 429 or r_recent_games.status_code == 429):
                        content = {'error': 'Limit reached'}
                        return Response(content, status=HTTP_429_TOO_MANY_REQUESTS)
                    else:
                        d_friends = r_friends.json()
                        d_games = r_games.json()
                        d_badges = r_badges.json()
                        d_bans = r_bans.json()
                        d_recent_games = r_recent_games.json()
                        keys['friends'] = d_friends['friendslist']
                        keys['games_owned'] = d_games['response']
                        keys['bans'] = d_bans['players']
                        keys['badges'] = d_badges['response']
                        keys['recent_games'] = d_recent_games['response']
                new_user = SteamProfile.objects.create(**keys)
                serializer = SteamProfileSerializer(new_user)
                return Response(serializer.data)

class TestList(generics.ListCreateAPIView):
    queryset = TestModel.objects.all()
    serializer_class = TestSerializer

class GetFriends(generics.RetrieveAPIView):
  queryset = SteamProfile.objects.all()
  serializer_class = SteamProfileSerializer
  def get(self, request, pk, *args, **kwargs):
    if SteamProfile.objects.filter(pk=self.kwargs.get('pk')).exists():
      profile = SteamProfile.objects.get(pk=self.kwargs.get('pk'))
      friends = profile.friends['friends']
      string = ''
      url = 'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=8BED1F5C904666F005800A4B9A5A1162&steamids='
      count = len(friends)
      combined_friends = []
      while count > 0:
        url = 'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=8BED1F5C904666F005800A4B9A5A1162&steamids='
        for friend in reversed(friends):
          string = string + friend['steamid'] + ','
          friends.pop()
          count -= 1
        completeurl = url + string
        r = requests.get(completeurl)
        data = r.json()
        for friend in data['response']['players']:
          combined_friends.append(friend)
      return Response(combined_friends)

class ShortProfile(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShortProfile.objects.all()
    serializer_class = ShortProfileSerializer