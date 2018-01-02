from player import Player
from human_player import HumanPlayer
import random

class Game:
    def __init__(self):
        self.numbers = {n for n in range(1, 91)}
        num_of_players, num_of_cards = self.ask_for_params()
        self.players = []
        self.done_win_conditions = []
        for i in range(0, num_of_players):
            if i == 0:
                self.players.append(HumanPlayer(num_of_cards))
            else:
                self.players.append(Player(num_of_cards))
        input('Press any button to play.')
        self.play()

    def play(self):
        while True:
            num = self.extract_number()
            for index, player in enumerate(self.players):
                result = player.next_turn(num)
                if result != None:
                    if result not in self.done_win_conditions:
                        self.done_win_conditions.append(result)
                        print('Player {} -> {}!'.format(index, result))
                        if result == 'tombola':
                            return

    def extract_number(self):
        num = random.choice(list(self.numbers))
        self.numbers.remove(num)
        print('The extracted number is: {}\n'.format(num))
        return num

    def ask_for_params(self):
        while True:
            try:
                num_of_players = int(input('How many players?\n'))
                if num_of_players < 1:
                    print('Num of players must be greater than 0.')
                else:
                    break
            except:
                print('Invalid input, please retry.')

        while True:
            try:
                num_of_cards = int(input('How many cards?\n'))
                if num_of_cards < 1:
                    print('Num of cards must be greater than 0.')
                else:
                    break
            except:
                print('Invalid input, please retry.')
        
        return num_of_players, num_of_cards