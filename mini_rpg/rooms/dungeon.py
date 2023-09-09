from rooms.room import Room

class Dungeon:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.rooms = []

    def generate_rooms(self):
        for _ in range(self.difficulty):
            difficulty_level = self.difficulty
            room = Room(difficulty_level)
            room.generate_content()
            self.rooms.append(room)