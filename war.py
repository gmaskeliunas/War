import random

class Player():
    def __init__(self, deck) -> None:
        self.deck = deck

    def __str__(self) -> str:
        return f"Player's deck: {self.deck}"

    def add_to_bottom(self):
        ...
    def draw_card(self):
        card = self.deck.popitem()
        return card

def assign_decks():
    suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
    ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    # numerical_ranks = ['14', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']
    deck_dict = {f'{suit} {rank}': rank for suit in suits for rank in ranks}
    for entry in deck_dict:
        if deck_dict[entry] =='Ace':
            deck_dict[entry] = '14'
        if deck_dict[entry] =='Jack':
            deck_dict[entry] = '11'
        if deck_dict[entry] =='Queen':
            deck_dict[entry] = '12'
        if deck_dict[entry] =='King':
            deck_dict[entry] = '13'
    # print(deck_dict,'\n')

    keys = list(deck_dict.keys())
    random.shuffle(keys)
    shuffled_deck_dict = dict()
    for key in keys:
        shuffled_deck_dict.update({key: deck_dict[key]})
    # print(shuffled_deck_dict)


    # deck = [(rank, suit) for suit in suits for rank in ranks]
    # random.shuffle(deck)
    # deck_split = (shuffled_deck_dict[:26],shuffled_deck_dict[26:])
    # deck1,deck2 = deck_split
    
    deck1 = dict(list(shuffled_deck_dict.items())[len(shuffled_deck_dict)//2:])
    deck2 = dict(list(shuffled_deck_dict.items())[:len(shuffled_deck_dict)//2])
    
    
    
    # split_index = len(deck) // 2
    # first_deck = deck[:split_index]
    # second_deck = deck[split_index:]
    return deck1,deck2

def card_match(player1, player2):
    
    player1_card = player1.draw_card()
    player2_card = player2.draw_card()
    
    if player1_card[1] == player2_card[1]:
        
        print("equal cards")
    

def game(player1, player2):
    game_pile = []
    while True:
        card_match(player1, player2)


def main():
    deck1, deck2 = assign_decks()
    player1 = Player(deck1)
    player2 = Player(deck2)
    
    
    card_match(player1,player2)
    
    
if __name__ == "__main__":
    main()