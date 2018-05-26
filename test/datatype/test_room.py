import pytest
import json
from datatype import Room

@pytest.fixture
def room(request):
    r = Room(id=1,name="Room",north=2,south=3,west=4, east=5, objects=[{"name":"Knife"}, {"name":"Pillow"}])
    return r

def test_find_one_object(room):
    obj = ["Knife"]
    found = json.dumps(room.find_objects(obj))
    result = json.dumps(obj)
    assert found == result

def test_find_more_objects(room):
    obj = ["Knife","Pillow"]
    found = json.dumps(room.find_objects(obj))
    result = json.dumps(obj)
    assert found == result

def test_get_south(room):
    assert room.get_south() == 3

def test_get_north(room):
    assert room.get_north() == 2

def test_get_east(room):
    assert room.get_east() == 5

def test_get_west(room):
    assert room.get_west() == 4

def test_get_id(room):
    assert room.get_id() == 1

def test_get_name(room):
    assert room.get_name() == "Room"


