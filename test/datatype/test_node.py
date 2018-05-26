from datatype import Room
from datatype import Node

import pytest


@pytest.fixture
def node(request):
    r = Room(id=1,name="Room",north=2,south=3,west=4, east=5, objects=[{"name":"Knife"}, {"name":"Pillow"}])
    return Node(r,2)

@pytest.fixture
def node_room_none(request):
    return Node(None,2)

def test_get_room(node):
    #result = '{"north": 2, "name": "Room", "west": 4, "objects": [{"name": "Knife"}, {"name": "Pillow"}], "east": 5, "id": 1, "south": 3}'
    #assert ''.join(sorted(node.get_room()._to_dict())) == ''.join(sorted(result))
    assert node.get_room() is not None

def test_get_room_none(node_room_none):
    assert node_room_none.get_room() is None

def test_get_link(node):
    assert node.get_link() == 2


