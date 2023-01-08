import random

def test_base(client):
    ''' TESTS '''
    get_index(client)


def get_index(client):
    index = client.get('/')
    assert index.status_code == 200
