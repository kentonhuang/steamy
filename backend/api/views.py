from django.shortcuts import render
from api.models import Game, SteamProfile, TestModel, ShortProfile, Badges
from api.serializers import GameSerializer, SteamProfileSerializer, TestSerializer, ShortProfileSerializer, BadgeSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import requests
import json
import time
import re

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
            return Response(serializer.data, status=status.HTTP_200_OK)
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
                return Response(serializer.data, status=status.HTTP_200_OK)

class TestList(generics.ListCreateAPIView):
    queryset = TestModel.objects.all()
    serializer_class = TestSerializer

class GetFriends(generics.RetrieveAPIView):
  queryset = SteamProfile.objects.all()
  serializer_class = SteamProfileSerializer
  def get(self, request, pk, *args, **kwargs):
    if SteamProfile.objects.filter(pk=self.kwargs.get('pk')).exists():
      profile = SteamProfile.objects.get(pk=self.kwargs.get('pk'))
      friends = profile.friends['friends'].copy()
      complete_friends = []
      nodata_friends = []
      for friend1 in reversed(friends):
        if ShortProfile.objects.filter(pk=friend1['steamid']).exists():
          short_prof = ShortProfile.objects.get(pk=friend1['steamid'])
          complete_friends.append(short_prof)
        else:
          nodata_friends.append(friend1)
      count = len(nodata_friends)
      while count > 0:
        combined_friends = []
        string = ''
        limit = 100;
        url = 'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=8BED1F5C904666F005800A4B9A5A1162&steamids='
        for friend2 in nodata_friends:
          string = string + friend2['steamid'] + ','
          limit = limit - 1
          count = count - 1
          if limit == 0:
            break
        completeurl = url + string
        nodata_friends = nodata_friends[100:]
        r = requests.get(completeurl)
        data = r.json()
        for friend3 in data['response']['players']:
          combined_friends.append(friend3)
        for friend4 in combined_friends:
          new_prof = {
            'id64': friend4['steamid'],
            'steam_url': friend4['profileurl'],
            'name': friend4['personaname'],
            'avatar': friend4['avatar'],
            'avatar_med': friend4['avatarmedium'],
            'avatar_full': friend4['avatarfull'],
            'status': friend4['personastate'],
            'visibility': friend4['communityvisibilitystate']
          }
          if 'lastlogoff' in friend4:
            new_prof['last_online'] = friend4['lastlogoff']
          if 'profilestate' in friend4:
            new_prof['profile_state'] = friend4['profilestate']
          if friend4['communityvisibilitystate'] != 1:
            if 'realname' in friend4:
                new_prof['real_name'] = friend4['realname']
            if 'timecreated' in friend4:
                new_prof['time_created'] = friend4['timecreated']
            if 'gameid' in friend4:
                new_prof['in_game'] = friend4['gameid']
            if 'gameextrainfo' in friend4:
                new_prof['in_game_name'] = friend4['gameextrainfo']
            if 'loccountrycode' in friend4:
                new_prof['loc_country'] = friend4['loccountrycode']
            if 'locstatecode' in friend4:
                new_prof['loc_state'] = friend4['locstatecode']
            if 'loccityid' in friend4:
                new_prof['loc_city'] = friend4['loccityid']
            if 'primaryclanid' in friend4:
                new_prof['primary_clan'] = friend4['primaryclanid']
          new_profile = ShortProfile.objects.create(**new_prof)
          complete_friends.append(new_profile)
        completeurl = ''
      serializer = ShortProfileSerializer(complete_friends, many=True)
      return Response(serializer.data, status=status.HTTP_200_OK)
    else:
      return Response({'Error': 'No user in the database with that ID'}, status=status.HTTP_404_NOT_FOUND)

class ShortProfiles(generics.ListCreateAPIView):
    queryset = ShortProfile.objects.all()
    serializer_class = ShortProfileSerializer

class BadgesView(generics.ListCreateAPIView):
  queryset = Badges.objects.all()
  serializer_class = BadgeSerializer

class GetBadges(generics.RetrieveAPIView):
  queryset = Badges.objects.all()
  serializer_class = BadgeSerializer
  def get(self, request, pk, *args, **kwargs):
    if SteamProfile.objects.filter(pk=self.kwargs.get('pk')).exists():
      profile = SteamProfile.objects.get(pk=self.kwargs.get('pk'))
      url = profile.steam_url + 'badges/'
      badges = profile.badges['badges'].copy()
      options = Options()
      options.add_argument("--headless") # Runs Chrome in headless mode.
      options.add_argument('--no-sandbox') # Bypass OS security model
      options.add_argument('--disable-gpu')  # applicable to windows os only
      options.add_argument('start-maximized') # 
      options.add_argument('disable-infobars')
      options.add_argument("--disable-extensions")

      capabilities = options.to_capabilities()

      badges_data = []
      data = []
      driver = webdriver.Remote("http://selenium-hub:4444/wd/hub", desired_capabilities=capabilities)
      driver.get(url)
      while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(0.1)
        page_content = BeautifulSoup(driver.page_source, 'html.parser')
        badges = page_content.findAll('div', {'class': ['badge_row', 'is_link']})
        for badge in badges:
          data.append(badge)

        try:
          element = driver.find_element_by_link_text('>')
        except:
          break
        is_disabled = 'disabled' in element.get_attribute("class")
        if(is_disabled):
          break
        element.click()
      
      for badge in data:
        description = badge.find('div',attrs={"class": "badge_info_description"})
        sub_title = description.find('div', attrs={"class": "badge_info_title"}).text.strip()
        
        level_xp = description.find('div',{"class": None}).text.strip()
        level_xp_join = " ".join(level_xp.split()).split(',')
        unlocked = description.find('div', attrs={"class": "badge_info_unlocked"}).text.strip()

        anchor = badge.find('a',attrs={"class":"badge_row_overlay"})
        link = anchor.get('href')

        badgeid = re.sub('https:\/\/steamcommunity.com\/id\/[a-zA-Z0-9]*\/', '', link).split('/')
        title = badge.find('div',attrs={"class":"badge_title"}).text.strip()
        title_text = " ".join(title.split())
        title_text = title_text.replace('View details', '')

        src = badge.find('img')
        img = src.get('src')

        level = ''
        keys = {}
        keys['unlocked'] = unlocked
        if(len(level_xp_join) == 2):
          keys['level'] = level_xp_join[0]
          keys['xp'] = level_xp_join[1]
          level = level_xp_join[0]

        else:
          keys['xp'] = level_xp_join[0]
        if badgeid[0] == 'badges':
          keys['badgeid'] = badgeid[1]
        if badgeid[0] == 'gamecards':
          keys['gameid'] = badgeid[1]
        
        if level != '':
          if level == 'Level 1':
            keys['image'] = img
          elif level == 'Level 2':
            keys['image2'] = img
          elif level == 'Level 3':
            keys['image3'] = img
          elif level == 'Level 4':
            keys['image4'] = img
          elif level == 'Level 5':
            keys['image5'] = img
        else:
          keys['image'] = img

        keys['description'] = title_text

        new_badge = Badges.objects.create(**keys)
        badges_data.append(new_badge)

      driver.quit()

      serializer = BadgeSerializer(badges_data, many=True)
      return Response(serializer.data, status=status.HTTP_200_OK)

      return Response({'Hey': 'Hows it going'}, status=status.HTTP_200_OK)
    else:
      return Response({'Error': 'No user in the database with that ID'}, status=status.HTTP_404_NOT_FOUND)