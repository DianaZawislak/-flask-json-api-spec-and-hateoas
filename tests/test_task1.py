""" Make the tests pass to make the cities endpoint work"""
# pylint: disable=redefined-outer-name, unused-argument

from app import app


def test_task1_routes():
    """Testing the routes to list records"""
    response = app.test_client().get('/')
    assert response.status_code == 200
    response = app.test_client().get('/countries/')
    assert response.status_code == 200
    response = app.test_client().get('/cities/')
    assert response.status_code == 200
