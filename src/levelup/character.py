class Character:
    name = ""
    position = (5,5)

    def __init__(self, character_name):
        self.name = character_name
        self.position = position
    
    def move(direction):
        new_pos = (0,0)
        match direction:
            case 'n':
                new_pos = (self.position[0], self.position[1]+1)
            case 's':
                new_pos = (self.position[0], self.position[1]-1)
            case 'w':
                new_pos = (self.position[0]-1, self.position[1])
            case 'e':
                new_pos = (self.position[0]+1, self.position[1])
        return new_pos
