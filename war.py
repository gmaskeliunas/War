import random

class Player():
    def __init__(self, deck) -> None:
        self.deck = deck

    def __str__(self) -> str:
        return f"Player's deck: {self.deck}"

    def add_to_bottom():
        ...


def assign_decks():
    suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
    ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    deck = [(rank, suit) for suit in suits for rank in ranks]
    random.shuffle(deck)
    split_index = len(deck) // 2
    first_deck = deck[:split_index]
    second_deck = deck[split_index:]
    return first_deck, second_deck

def game():
    while True:
        ...

def main():
    deck1, deck2 = assign_decks()
    player1 = Player(deck1)
    player2 = Player(deck2)
    game(player1, player2)

if __name__ == "__main__":
    main()