# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
  def __init__(self, name, current_room):
    self.name = name
    self.current_room = current_room
    self.player_items = []
  def __str__(self):
    return str(self.__dict__)
  def get_item(self):
    if self.current_room.items:
      return f'there are {self.current_room.item_list} here.'