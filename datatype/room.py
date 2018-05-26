import json

class Room:
    def __init__(self,id=None,name=None,north=None,south=None,west=None, east=None, objects=None):
        self.id = id
        self.name = name
        self.north = north
        self.south = south
        self.west = west
        self.east = east
        self.objects = objects
        if objects is not None:
            self.raw_objects = [elem["name"] for elem in self.objects]
        else:
            self.raw_objects = []

    def __repr__(self):
        return json.dumps(self._to_dict())

    def _to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "north": self.north,
            "south": self.south,
            "west": self.west,
            "east": self.east,
            "objects": self.objects
        }

    def get_south(self):
        return self.south

    def get_north(self):
        return self.north

    def get_east(self):
        return self.east

    def get_west(self):
        return self.west

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_objects(self):
        return self.get_objects()

    def find_objects(self,list_objects_to_find):
        found_objects = []
        for object in list_objects_to_find:
            if object in self.raw_objects:
                found_objects.append(object)
        
        return found_objects
