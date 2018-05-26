import pytest
#import os, sys

from parser import Parser
from os import environ as env

project_dir = env['PROJECT_DIR']
#project_dir = os.path.realpath(__file__).split("/test")[0]
#sys.path.append(project_dir)

@pytest.fixture
def parser(request):
    p = Parser('{}/test/datasource/map.json'.format(project_dir))
    p.parse()
    return p

def test_get_hash_rooms(parser):
    assert len(parser.get_hash_rooms()) == 7

def test_get_raw_map(parser):
    assert parser.get_raw_map() is not None

    
