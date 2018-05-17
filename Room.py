class Room():

    name= ""
    description= None
    linked_rooms={}
    character= None
    item = None

    def limit (self, room_name):
        self.name = room_name

    #r = Room("a")
        #r.get_charcater()
        #r.charecter

    def set_charcter(self, new_charcater):
        self.charcter = new_charcter

    def get_charcter(self):
        return se;f.chacrtyer

    def set_name(self, now_name):
        self.name= new_name

    def get_name(self):
        return self.name

    def self_description(self, new_description):
        self.description = new_description

    def get_description(self):
        return self.decription

    def set_item(self, new_item):
        self.item = new_item

    def get_item(self):
        return self.item

    def describe(self):
        print(self.description)

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link
        #comment later
        print(self.name + " linked rooms: " + repr(self.linked_rooms))

    def get_details():
        print(self.get_name())
        print('-'*15)
        print(self.get_description())
        if direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print("The {} is {}.".format(room.get_name(), direction))

    def move(self, direction):
        if direction in self.linked_rooms:
              return self.linked_room[direction]
        else:
              print("You can't go that way!")
              return self
