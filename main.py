from room import Room
# file           class

kitchen= Room("kitchen")
kitchen.set_description("A desk and dirty room buzzing with flies.")

dining_hall = Room("Dining Hall")
dining_hall.set_descrpition("A large room, with ornate golden decorations on each wall.")

ballroom = Room("Ballroom")
ballroom.set_descrpition("A vast room with a shiny floor, Huge candlesticks guard the entrance.")

kitchen.link_room(dining-hall, "south")

game_room = Room ("Game Room")
game_room.set_decription("A blue colored room with games such as pac man.")

sauna_room = Sauna ("Sauna Room")
sauna_room.set_description("A hot room where people can go to lose weight and relax.")

dining_hall.link_room(kitchen, "north")
dining_hall.link_room(hallroom, "west")
ballroom.link_room(dining_hall, "east")
kitchen.link_room(game_room, "south")
dining_hall.link_room(sauna, "east")


current_room = kitchen
while True:
    print('\n')
    current_room.get_details()
    command = input('> ')
    current_room = current_room.move(command)
