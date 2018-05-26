from datatype import Route
from datatype import Room
import pytest
import json

@pytest.fixture
def route(request):
    room = Room(id=1,name="Room",north=2,south=3,west=4, east=5, objects=[{"name":"Knife"}, {"name":"Pillow"}])
    route = Route(room, ["Knife","Pillow"])
    return route

@pytest.fixture
def route_no_object(request):
    room = Room(id=1,name="Room",north=2,south=3,west=4, east=5, objects=[])
    route = Route(room, [])
    return route

def test_get_room_id(route):
    assert route.get_room_id() == 1

def test_get_room_name(route):
    assert route.get_room_name() == "Room"

def test_get_objects_found(route):
    assert route.get_objects_found() == 'Knife Pillow'


def test_get_objects_no_found(route_no_object):
    assert route_no_object.get_objects_found() == 'None'
