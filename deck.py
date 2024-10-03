from hand import Card
import random

class Deck:
    def __init__(self):
        self.deck = self.__setup_52_cards()
        self.shuffle()

    def __setup_52_cards(self):
        """Create a standard deck of 52 cards."""
        suits = [1, 2, 4, 8]  # Suits: Spades, Diamonds, Hearts, Clubs
        ranks = range(2, 15)  # Card ranks: 2 to Ace (represented as 14)
        return [Card(rank, suit) for rank in ranks for suit in suits]

    def shuffle(self):
        """Shuffle the deck of cards."""
        random.shuffle(self.deck)

    def draw_card(self):
        """Draw a single card from the deck."""
        return self.deck.pop()

    def draw_cards(self, num):
        """Draw multiple cards from the deck."""
        return [self.draw_card() for _ in range(num)]

    def reset(self):
        """Reset the deck by recreating and reshuffling the cards."""
        self.deck = self.__setup_52_cards()
        self.shuffle()

    def size(self):
        """Return the current size of the deck."""
        return len(self.deck)
