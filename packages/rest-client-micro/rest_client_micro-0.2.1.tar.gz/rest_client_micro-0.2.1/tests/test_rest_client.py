"""Test cases for RESTClient"""
from src.rest_client_micro.rest_client import RESTClient as rc
from src.rest_client_micro.rest_object import RESTObject as ro


def test_client():
    rest_object = ro()
    rest_object.endpoint = 'https://api.scryfall.com/cards/named'
    rest_object.params = {'exact': 'Overgrown Tomb'}
    rest_client = rc()
    rc.debug = True
    result = rest_client.execute(rest_object)

    assert result['error'] is False
    assert result['response'].startswith('{"object":"card"')
