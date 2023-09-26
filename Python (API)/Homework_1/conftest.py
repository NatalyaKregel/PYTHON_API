import pytest
import requests
import yaml

S = requests.Session()

with open('config.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)


@pytest.fixture()
def get_token():
    res = S.post(url=data['url_auto'], data={'username': data['username'], 'password': data['password']})
    return res.json()['token']


@pytest.fixture()
def description_post():
    return 'Maine Coon'






