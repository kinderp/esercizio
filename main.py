from parser import Parser
from datatype import Map
from datatype import Room
from datatype import Router

import argparse

def parsing(filename):
    p = Parser(filename)
    p.parse()
    hash_rooms = p.get_hash_rooms()
    raw_map = p.get_raw_map()
    return (raw_map, hash_rooms)

def main(filename,id_root,object_to_find):

    raw_map, hash_rooms = parsing(filename)

    my_map = Map(raw_map, hash_rooms)
    root = hash_rooms[id_root]
    router = Router(root, my_map, object_to_find)
    router.get_route()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='find a route from a root!')
    parser.add_argument('-f', action="store", dest="filename", help="your map (json format)")
    parser.add_argument('-i', action="store", dest="root", type=int, help="your root room id")
    parser.add_argument('-o', action='store', dest='objects', nargs='+')
    args = parser.parse_args()
    main(args.filename, args.root, args.objects)
