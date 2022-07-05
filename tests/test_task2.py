""" Make the tests pass to make the cities endpoint work"""
# pylint: disable=redefined-outer-name, unused-argument

from app import app


def test_task2_routes():
    """Testing Routest to get a record"""
    response = app.test_client().get('/countries/1')
    assert response.status_code == 200
    response = app.test_client().get('/cities/1')
    assert response.status_code == 200
