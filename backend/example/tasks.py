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
        r = requests.get('http://store.steampowered.com/api/appdetails?appids=' + str(id))
        if(r.status_code == 200):
            data = r.json()
            if(data[str(id)]['success'] == True):
                logger.info(data[str(id)]['data']['type'])
                logger.info(data[str(id)]['data']['name'])
                if 'developers' in data[str(id)]['data']:
                    logger.info(data[str(id)]['data']['developers'])
                if 'publishers' in data[str(id)]['data']:
                    logger.info(data[str(id)]['data']['publishers'])
                if 'price_overview' in data[str(id)]['data']:
                    logger.info(data[str(id)]['data']['price_overview'])
                if 'header_image' in data[str(id)]['data']:
                    logger.info(data[str(id)]['data']['header_image'])
                if 'detailed_description' in data[str(id)]['data']:
                    logger.info(data[str(id)]['data']['detailed_description'])
                if 'detailed_description' in data[str(id)]['data']:
                    logger.info(data[str(id)]['data']['short_description'])
                if 'dlc' in data[str(id)]['data']:
                    logger.info(data[str(id)]['data']['dlc'])
                if 'genres' in data[str(id)]['data']:
                    logger.info(data[str(id)]['data']['genres'])
                if 'platforms' in data[str(id)]['data']:
                    logger.info(data[str(id)]['data']['platforms'])
                if 'release_date' in data[str(id)]['data']:
                    logger.info(data[str(id)]['data']['release_date'])
            # datastore['applist']['apps'].pop()
            # with open("game.json", 'w') as g:
            #     json.dump(datastore, g, ensure_ascii=False)
        if(r.status_code == 429):
            logger.info('Breaking Limit Reached')
            break

    
    