"""Dred.py - An API wrapper for drednot.io, an IO game."""
import json
import requests

# for now, I will only get stats from prod, not the test server
BASE_URL = "https://pub.drednot.io/prod/econ/"

def item_scheme() -> list:
    """Fatches and returns the latest item scheme, in a python dictionary."""
    resp = requests.get(f"{BASE_URL}item_schema.json")
    return json.loads(resp.content)

def get_item_stats(item: str) -> dict:
    """Find an item in the item scheme, and only return its stats."""
    scheme = item_scheme()
    # not the most efficent, later I will redo this
    for i in scheme:
        if i['name'] == item:
            return i

