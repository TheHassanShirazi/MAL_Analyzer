import json
import requests
import time
from datetime import datetime

all_fields = [
    "id",
    "title",
    "main_picture",
    "alternative_titles",
    "start_date",
    "end_date",
    "synopsis",
    "mean",
    "rank",
    "popularity",
    "num_list_users",
    "num_scoring_users",
    "nsfw",
    "genres",
    "created_at",
    "updated_at",
    "media_type",
    "status",
    # "my_list_status",
    "num_episodes",
    "start_season",
    "broadcast",
    "source",
    "average_episode_duration",
    "rating",
    "studios",
    # "pictures",
    # "background",
    # "related_anime",
    # "related_manga",
    # "recommendations",
    # "statistics"
]


def request(access_token, curr_offset):
    url = 'https://api.myanimelist.net/v2/manga/ranking'
    response = requests.get(url,
                            headers={'Authorization': f'Bearer {access_token}'},
                            params={
                                'ranking_type': 'all',
                                'limit': 500,
                                'offset': curr_offset,
                                'fields': ','.join(all_fields)
                            })
    response.raise_for_status()
    response.close()
    return response.json()


def scrape(access_token):
    date_string = datetime.now().isoformat().replace(':', '')
    with open(f'database2_{date_string}.json', 'w') as file:
        file.write('[\n')
        delim = ''
        for offset in range(0, 100000, 500):
            print(f'Getting {offset + 1} through {offset + 500}')
            data = request(access_token, offset)['data']
            if len(data) == 0:
                break
            for d in data:
                file.write(delim)
                delim = ',\n'
                json.dump(d['node'], file, indent=4)
            time.sleep(0.3)
        file.write("\n]")
    print('Done')


if __name__ == '__main__':
    with open('token.json') as file:
        token = json.load(file)['access_token']
        scrape(token)
