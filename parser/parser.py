from datatype import Room
import json

class Parser:
    def __init__(self,filename):
        self.hash_rooms = {}
        self.raw_rooms = None
        self.raw_map = None
        self.filename = filename

    def parse(self):
        with open(self.filename) as raw_map:
            self.raw_map = json.load(raw_map)

        for room in self.raw_map["rooms"]:
            self.hash_rooms[room["id"]] = Room(**room)

    def get_hash_rooms(self):
        return self.hash_rooms

    def get_raw_map(self):
        return self.raw_map["rooms"]
