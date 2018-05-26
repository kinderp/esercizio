class Route:
    def __init__(self,room,objects_found):
        self.room = room
        self.objects_found = objects_found

    def get_room_id(self):
        return self.room.get_id()

    def get_room_name(self):
        return self.room.get_name()

    def get_objects_found(self):
        if len(self.objects_found) > 0:
            return " ".join(self.objects_found)
        else:
            return "None"
