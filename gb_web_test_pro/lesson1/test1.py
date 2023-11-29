from task1 import avt, create_post, get_post


def test_pagination_check_id(authorization_token):
    res = avt(authorization_token)
    list_id = []
    for i in res:
        list_id.append(i['id'])
    assert 90517 in list_id, 'Test Failed'


def test_post_method(authorization_token):
    rnd_uuid, post_id = create_post(authorization_token)
    post_json = get_post(authorization_token, post_id)
    assert 1 == 1 and post_json is not None and post_json['id'] == post_id and rnd_uuid in post_json[
        'content'], 'Test Failed'
