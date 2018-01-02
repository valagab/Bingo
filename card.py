from copy import copy

import random

class Card:
    def __init__(self, rows = 3, cols = 5):
        self.rows = rows
        self.cols = cols

    def generate_numbers(self):
        self.original_numbers = [set() for i in range(0, self.rows)] # List Comprehensions
        numbers = {n for n in range(1, 91)} # set
        for row_index, row in enumerate(range(0, self.rows)):
            for col in range(0, self.cols):
                num = random.choice(list(numbers))
                self.original_numbers[row_index].add(num)
                numbers.remove(num)
        self.inizialize()

    def inizialize(self):
        self.current_numbers = copy(self.original_numbers)
    
    def show(self):
        stringed_card = ''
        for row in self.current_numbers:
            for col in row:
                stringed_card += str(col) + ' '
            stringed_card += '\n'
        print(stringed_card)

    def remove_number(self, called_num):
        for row in self.current_numbers:
            try:
                row.remove(called_num)
            except Exception:
                pass