import requests
import yaml

with open('config.yaml') as f:
    data = yaml.safe_load(f)

s = requests.Session()


def test_step1_create_new_post(get_token):
    '''Создание нового поста и проверка соответствия фразы в description'''
    res = s.post(url=data['url_post'], headers={'X-Auth-Token': get_token},
                 params={"title": data['title_post'],
                         'description': data["description_post"],
                         'content': data['content_post']})

    res = s.get(url=data['url_post'], headers={"X-Auth-Token": get_token}).json()['data']
    res_title = [i['title'] for i in res]
    assert data['description_post'] in res_title, 'Fail test_step1'

