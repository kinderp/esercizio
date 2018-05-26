import pytest
#import os, sys

from parser import Parser
from datatype import Map
from datatype import Node
from datatype import Room

from os import environ as env
project_dir = env['PROJECT_DIR']

#project_dir = os.path.realpath(__file__).split("/test")[0]
#sys.path.append(project_dir)

@pytest.fixture
def my_map(request):
    p = Parser('{}/test/datasource/map.json'.format(project_dir))
    p.parse()
    hash_rooms = p.get_hash_rooms()
    raw_map = p.get_raw_map()
    m = Map(raw_map, hash_rooms)
    return m



def test_get_neighbors(my_map):
    assert len(my_map.get_neighbors(1)) == 2

def test_get_num_nodes(my_map):
    assert my_map.get_num_nodes() == 7

def test_add_node_new_key(my_map):
    r = Room(id=1,name="Room1",north=2,south=3,west=4, east=5, objects=[{"name":"Knife"}, {"name":"Pillow"}])
    n = Node(r,5)
    my_map._add_node(12,n)
    assert my_map.get_num_nodes() == 8

def test_add_node_existent_key(my_map):
    r = Room()
    n = Node(r,-1)
    my_map._add_node(1,n)
    assert len(my_map.get_neighbors(1)) == 3
    

