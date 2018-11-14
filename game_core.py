from random import choice

class Game:
    def hash(self):
        return hash(tuple(tuple(row) for row in self.__grid))

    def __init__(self):
        self.__score = 0
        self.__grid = [[None]*4 for _ in range(4)]
        self.__add_random_tile__()
        self.__add_random_tile__()

    def __add_random_tile__(self):
        candidates = list()
        ## get list of all empty tiles
        for y in range(4):
            for x in range(4):
                if None == self.__grid[y][x]:
                    candidates.append({'x' : x, 'y' : y})
        # return False if no tile is empty
        if 0 == len(candidates):
            return False
        else:
            cooridnates = choice(candidates)
            self.__grid[cooridnates['y']][cooridnates['x']] = choice([2]*9 + [4])
            return True

    def __push_left(self):
        hash_beginning = self.hash()
        for y in range(4):
            # slides tiles to the left
            for i in range(4):
                for x in range(3):
                    if None == self.__grid[y][x]:
                        self.__grid[y][x] =  self.__grid[y][x+1]
                        self.__grid[y][x+1] = None
            # go through all adjacent tiles
            for x in range(3):
                # merge equal tiles
                if None != self.__grid[y][x] and self.__grid[y][x] == self.__grid[y][x+1]:
                    self.__grid[y][x] = self.__grid[y][x]*2
                    self.__grid[y][x+1] = None
                    self.__score += self.__grid[y][x]
            # slides tiles to the left
            for i in range(4):
                for x in range(3):
                    if None == self.__grid[y][x]:
                        self.__grid[y][x] =  self.__grid[y][x+1]
                        self.__grid[y][x+1] = None
        if hash_beginning != self.hash():
            self.__add_random_tile__()
            return True
        else:
            return False

    def __rotate_right(self):
        self.__grid = [list(t) for t in zip(*(self.__grid[::-1]))]

    def get_state(self):
        return self.__grid.copy()

    def get_score(self):
        return self.__score

    def up(self):
        self.__rotate_right()
        self.__rotate_right()
        self.__rotate_right()
        result = self.__push_left()
        self.__rotate_right()
        return result
        
    def down(self):
        self.__rotate_right()
        result = self.__push_left()
        self.__rotate_right()
        self.__rotate_right()
        self.__rotate_right()
        return result

    def left(self):
        return self.__push_left()

    def right(self):
        self.__rotate_right()
        self.__rotate_right()
        result = self.__push_left()
        self.__rotate_right()
        self.__rotate_right()
        return result
