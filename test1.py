

from task1 import avt


def test_post(authorization_token):
    res = avt(authorization_token)
    list_id = []
    for i in res['data']:
        list_id.append(i['id'])
        print(i['id'], type(i))
    assert 90517 in list_id
