from hand import Card
from deck import Deck

# Initialize the deck
deck = Deck()

# Check deck size after initialization
print(f"Initial deck size: {deck.size()}")  # Expected: 52

# Draw one card from the deck
card = deck.draw_card()
print(f"Drawn card: {card}")

# Check deck size after drawing one card
print(f"Deck size after drawing one card: {deck.size()}")  # Expected: 51

# Draw five cards from the deck
hand = deck.draw_cards(5)
print("Drawn hand of 5 cards:")
for card in hand:
    print(card)

# Check deck size after drawing five more cards
print(f"Deck size after drawing five cards: {deck.size()}")  # Expected: 46

# Reset the deck
deck.reset()
print(f"Deck size after reset: {deck.size()}")  # Expected: 52

# Check if the deck is shuffled
print("Shuffling deck and drawing top card after reset:")
card_after_reset = deck.draw_card()
print(f"Top card after reset: {card_after_reset}")
