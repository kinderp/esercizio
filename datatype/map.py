from .node import Node
import pdb
import json

class Map:
    def __init__(self,raw_map, hash_rooms):
        self.raw_map = raw_map
        self.hash_rooms = hash_rooms
        self.map = {}
        self._build_map()
        self.num_nodes = len(self.map)

        #self._print_map()

    def get_neighbors(self,id):
        return self.map[id]

    def get_num_nodes(self):
        return self.num_nodes

    def _build_map(self):
        for room in self.raw_map:


            current_id_room = room["id"]
            current_room = self.hash_rooms[current_id_room]

            if current_room.get_north() is not None:
                id_north_room = current_room.get_north()
                north_room = self.hash_rooms[id_north_room]
                tmp_node = Node(north_room,"north")
                self._add_node(current_id_room,tmp_node)

            if current_room.get_south() is not None:
                id_south_room = current_room.get_south()
                south_room = self.hash_rooms[id_south_room]
                tmp_node = Node(south_room, "south")
                self._add_node(current_id_room,tmp_node)

            if current_room.get_east() is not None:
                id_east_room = current_room.get_east()
                east_room = self.hash_rooms[id_east_room]
                tmp_node = Node(east_room, "east")
                self._add_node(current_id_room,tmp_node)

            if current_room.get_west() is not None:
                id_west_room = current_room.get_west()
                west_room = self.hash_rooms[id_west_room]
                tmp_node = Node(west_room, "west")
                self._add_node(current_id_room,tmp_node)


    def _add_node(self, id, node):
        if id in self.map:
            self.map[id].append(node)
        else:
            self.map[id] = []
            self.map[id].append(node)
            self.num_nodes = len(self.map)

    def _print_map(self):
        print(json.dumps(self.map))
