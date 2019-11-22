# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.item_list = []
    def __str__(self):
        return str(self.__dict__)
    def add_item(self, item):
        self.item_list.append(item)
    def display_item(self):
        # initualize empty output for user
        output = ''
        # if no item in room, display nothing
        if len(self.item_list) == 0:
            return None
        else:
            # display all items in the room for the user
            for item in self.item_list:
                output += f"{item.name}, {item.desc}"
        return output