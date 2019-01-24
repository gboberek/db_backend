import sys
import random

class mine_locator(object):

    def init(self, number_of_mines, dimension):
        self.number_of_mines = number_of_mines
        self.dimension = dimension

    def mine_locator(self):
        number_of_empty_places = self.dimension - self.number_of_mines
        list_of_mines = [1]* self.number_of_mines + [0]*number_of_empty_places
        random.shuffle(list_of_mines)
        print list_of_mines




