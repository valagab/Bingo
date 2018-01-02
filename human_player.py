from player import Player

class HumanPlayer(Player):
    def __init__(self, num_of_cards):
        super().__init__(num_of_cards)

    def build_cards(self):
        while True:
            super().build_cards()
            try:
                ok = int(input('Do you like the cards? yes=1, no=2\n'))
                if ok == 1:
                    return
            except:
                print('Invalid input, please retry.')

    def next_turn(self, extracted_number: int) -> str:
        input('Press any button to continue.\n')
        return super().next_turn(extracted_number)
