game
    players # lista di player
    start # numero di cartelle, se cartella ok
    play # inizio partita

player
    cards = lista di cartelle
    check_rows(number of rows)
    build_cards genera card
    next_turn pass

human player(player)
    next_turn input invio
    build_cards genera card se va bene altrimenti rigeneri

card
    original_numbers = lista di 3 set
    current_numbers = lista di 3 set corrente
    generate_numbers
    show

#-----------------------------------------------------------------

Git: comandi base come status, stage, commit, push e pull, branch
Basi di python: if, for, while, classi, funzioni, moduli (from import), liste, dizionari, tuple, set, ereditarietà
SQL: comandi principali
Django: cos'è un applicazione, cosa sono i modelli, rivedi il mini progetto, rivedi il tutorial per creare la prima applicazione in Django

#-----------------------------------------------------------------

#main.py

game
    players # lista di player
    start # numero di cartelle, se cartella ok
    play # inizio partita
    extract_next_number 

player
    cards = lista di cartelle
    check_rows(number of rows)
    build_cards genera card
    next_turn pass

human player(player)
    next_turn input invio
    build_cards genera card se va bene altrimenti rigeneri

card
    original_numbers = lista di 3 set
    current_numbers = lista di 3 set corrente
    generate_numbers
    show

#-----------------------------------------------------------------

#card.py

from copy import copy

import random

class Card:
    def __init__(self, rows = 3, cols = 5):
        self.rows = rows
        self.cols = cols

    def generate_numbers(self):
        self.original_numbers = [set() for i in range(0, self.rows)] # List Comprehensions
        numbers = {n for n in range(0, 91)} # set
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

#-----------------------------------------------------------------

#player.py

from card import Card
from conf import WIN_CONDITIONS

class Player:
    def __init__(self, num_of_cards):
        self.cards = []
        for i in range(0, num_of_cards):
            self.cards.append(Card())

    def check_rows(self):
        for card in self.cards:
            rows_completed = 0
            for row in card.current_numbers:
                if len(row) == 0:
                    rows_completed += 1
            for win_condition in WIN_CONDITIONS.keys():
                if rows_completed == WIN_CONDITIONS[win_condition]:
                    return win_condition
        return ''
                    
    def build_cards(self):
        for card in self.cards:
            card.generate_numbers()
            card.show()
        print('\n\n')
    
    def next_turn(self, extracted_number):
        for card in self.cards:
            card.remove_number(extracted_number)
        return self.check_rows()

#-----------------------------------------------------------------

#human_player.py(player)

from player import Player

class HumanPlayer(Player):
    def __init__(self, num_of_cards):
        super().__init__(self, num_of_cards)

    def build_cards(self):
        while True:
            super.build_cards()
            try:
                ok = int(input('Do you like the cards? yes=1, no=2'))
                if ok == 1:
                    return
            except:
                print('Invalid input, please retry.')

    def next_turn(self):
        input('Press any button to continue.')
        super.next_turn()

#-----------------------------------------------------------------

#game.py

from player import Player
from human_player import HumanPlayer

class Game:
    def __init__(self):
        self.numbers = {n for n in range(0, 91)}
        num_of_players, num_of_cards = self.ask_for_params()
        self.players = []
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
                if result != '':
                    print('Player {} -> {}!'.format(index, result))
                    if result == 'tombola':
                        return

    def extract_number(self):
        num = random.choice(list(self.numbers))
        self.numbers.remove(num)
        return num

    def ask_for_params(self):
        while True:
            try:
                num_of_players = int(input('How many players?'))
                if num_of_players < 1:
                    print('Num of players must be greater than 0.')
            except:
                print('Invalid input, please retry.')

        while True:
            try:
                num_of_cards = int(input('How many cards?'))
                if num_of_cards < 1:
                    print('Num of cards must be greater than 0.')
            except:
                print('Invalid input, please retry.')
        
        return num_of_players, num_of_cards

#-----------------------------------------------------------------


#-----------------------------------------------------------------

#conf.py

WIN_CONDITIONS = {
    'cinquina': 1,
    'decina': 2,
    'tombola': 3
}

#-----------------------------------------------------------------