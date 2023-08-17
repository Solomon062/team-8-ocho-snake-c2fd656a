from levelup.position import Position
from levelup.direction import Direction

class Character:

    def __init__(self, character_name):
        self.name = character_name
        self.current_position = Position(-100, -100)

    
    def move(self, direction):
        match direction:
            case Direction.EAST:
                self.current_position.x += 1
            case Direction.SOUTH:
                self.current_position.y -= 1
            case Direction.WEST:
                self.current_position.x -= 1
            case Direction.NORTH:
                self.current_position.y += 1
