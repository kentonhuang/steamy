from celery.task.schedules import crontab
from celery import shared_task
from celery.utils.log import get_task_logger

from api.models import Game

import json
import requests

logger = get_task_logger(__name__)

@shared_task
def get_game_info():
    logger.info('get_game_info STARTING')
    with open("game.json", 'r') as f:
        datastore = json.load(f)

    for i in reversed(datastore["applist"]["apps"]):
        id = i['appid']
        if Game.objects.filter(pk=id).exists():
            logger.info(str(id) + 'exists')
            datastore['applist']['apps'].pop()
            with open("game.json", 'w') as g:
                json.dump(datastore, g, ensure_ascii=False)
            continue
        r = requests.get('http://store.steampowered.com/api/appdetails?appids=' + str(id))
        if(r.status_code == 200):
            data = r.json()
            if(data[str(id)]['success'] == True):
                keys = {
                    'id' : i['appid'],
                    'game_type' : data[str(id)]['data']['type'],
                    'name' : data[str(id)]['data']['name'],
                }
                if 'developers' in data[str(id)]['data']:
                    keys['dev'] = data[str(id)]['data']['developers']
                if 'publishers' in data[str(id)]['data']:
                    keys['pub'] = data[str(id)]['data']['publishers']
                if 'price_overview' in data[str(id)]['data']:
                    keys['price'] = data[str(id)]['data']['price_overview']
                if 'header_image' in data[str(id)]['data']:
                    keys['image'] = data[str(id)]['data']['header_image']
                if 'detailed_description' in data[str(id)]['data']:
                    keys['description'] = data[str(id)]['data']['detailed_description']
                if 'short_description' in data[str(id)]['data']:
                    keys['short_desc'] = data[str(id)]['data']['short_description']
                if 'dlc' in data[str(id)]['data']:
                    keys['dlc'] = data[str(id)]['data']['dlc']
                if 'genres' in data[str(id)]['data']:
                    keys['genres'] = data[str(id)]['data']['genres']
                if 'platforms' in data[str(id)]['data']:
                    keys['platforms'] = data[str(id)]['data']['platforms']
                if 'release_date' in data[str(id)]['data']:
                    keys['release_date'] = data[str(id)]['data']['release_date']
                new_game = Game.objects.create(**keys)
                logger.info('Created new Game in db!' + str(id))
            datastore['applist']['apps'].pop()
            with open("game.json", 'w') as g:
                json.dump(datastore, g, ensure_ascii=False)
        if(r.status_code == 429):
            logger.info('Breaking Limit Reached')
            break

    
    