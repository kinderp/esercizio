import json

class Node:
    def __init__(self,room,link):
        self.room = room
        self.link = link

    def __repr__(self):
        return json.dumps(self._to_dict())

    def get_room(self):
        return self.room

    def get_link(self):
        return self.link

    def _to_dict(self):
        return {
            "room": self.room._to_dict(),
            "link": self.link
        }

