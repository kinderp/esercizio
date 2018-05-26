from datatype import Route

class Router:
    def __init__(self, root, my_map, objects_to_find):
        self.my_map = my_map
        self.objects_to_find = objects_to_find
        self.visited = [0]* self.my_map.get_num_nodes()
        self.route = []
        self.traverse(root)

    def traverse(self,root):
        objects_found = root.find_objects(self.objects_to_find)

        index = root.get_id()
        self.visited[index-1] = 1

        r = Route(root,objects_found)
        self.route.append(r)

        #print("visiting node {} ... found {}".format(index, r.get_objects_found()))
        for node in self.my_map.get_neighbors(index):
            node_index = node.get_room().get_id()
            if self.visited[node_index-1]:
                continue
            else:
                self.traverse(node.get_room())
            r_back = Route(root, [])
            self.route.append(r_back)

    def get_route(self):
        print("%-2s %-15s %-20s" % ("ID", "Room", "Object collected"))
        for r in self.route:
            print("%-2s %-15s %-20s" % (r.get_room_id(), r.get_room_name(), r.get_objects_found()))





