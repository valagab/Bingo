from card import Card
from conf import WIN_CONDITIONS

class Player:
    def __init__(self, num_of_cards):
        self.cards = []
        for i in range(0, num_of_cards):
            self.cards.append(Card())
        self.build_cards()

    def check_rows(self):
        for card in self.cards:
            rows_completed = 0
            for row in card.current_numbers:
                if len(row) == 0:
                    rows_completed += 1
            for win_condition in WIN_CONDITIONS.keys():
                if rows_completed == WIN_CONDITIONS[win_condition]:
                    return win_condition
                    
    def build_cards(self):
        for card in self.cards:
            card.generate_numbers()
            card.show()
        print('\n')
    
    def next_turn(self, extracted_number):
        for card in self.cards:
            card.remove_number(extracted_number)
        return self.check_rows()
