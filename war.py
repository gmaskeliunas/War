import random

class Player():
    def __init__(self, deck) -> None:
        self.deck = deck

    def __str__(self) -> str:
        return f"Player's deck: {self.deck}"

    def add_cards(self, cards):
        for card in cards:
            print(card)
            self.deck.update(card)
    def draw_card(self):
        card = self.deck.popitem()
        return card

def assign_decks():
    suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
    ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
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
    keys = list(deck_dict.keys())
    random.shuffle(keys)
    shuffled_deck_dict = dict()
    for key in keys:
        shuffled_deck_dict.update({key: deck_dict[key]})

    deck1 = dict(list(shuffled_deck_dict.items())[len(shuffled_deck_dict)//2:])
    deck2 = dict(list(shuffled_deck_dict.items())[:len(shuffled_deck_dict)//2])
    return deck1, deck2

def card_match(player1, player2):

    while True:
        player1_card = player1.draw_card()
        player2_card = player2.draw_card()
        cards = [player1_card, player2_card]
        if player1_card[1] > player2_card[1]:
            cards.append(player1_card)
            player1.add_cards(cards)
        elif player1_card[1] < player2_card[1]:
            cards.append(player2_card)
            player2.add_cards(cards)
        elif player1_card[1] == player2_card[1]:
            ...
        print(len(player1.deck))



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