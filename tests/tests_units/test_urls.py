from tests.conftest import client
import pytest

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200


def test_showSummary(client):
    email = 'john@simplylift.co'
    wrong_mail = ''

    response = client.post('/showSummary', data={'email': email})
    assert response.status_code == 200

    response2 = client.post('/showSummary', data={'email': wrong_mail})
    assert b'<h3>' in response2.data