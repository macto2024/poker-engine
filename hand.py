class Card:
    Suits = {
        1: "Spade",
        2: "Diamond",
        4: "Heart",
        8: "Clover"
    }
    
    Ranks = {
        2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
        8: '8', 9: '9', 10: '10', 11: 'J', 12: 'Q', 13: 'K', 14: 'A'
    }
    
    RANK_MASKS = {
        2: 0b1000000000000,
        3: 0b0100000000000,
        4: 0b0010000000000,
        5: 0b0001000000000,
        6: 0b0000100000000,
        7: 0b0000010000000,
        8: 0b0000001000000,
        9: 0b0000000100000,
        10: 0b0000000010000,
        11: 0b0000000001000,  # Jack
        12: 0b0000000000100,  # Queen
        13: 0b0000000000010,  # King
        14: 0b0000000000001   # Ace
    }
    
    def __init__(self, rank, suit):
        self.rank = rank;
        self.suit = suit;
    
    
    def __str__(self):
        # return human readable card
        return f"{Card.Ranks[self.rank]} of {Card.Suits[self.suit]}"
    
    def encode(self):
        # Encode the card into an 8-bit integer
        return self.suit << 4 | self.rank
    
    @classmethod
    def decode(cls, encoded_card):
        # Decode an 8-bit integer into a card
        suit = (encoded_card >> 4) & 0xF
        rank = encoded_card & 0xF
        return cls(rank, suit)
        
    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit
    
    def __lt__(self, other):
        return self.rank < other.rank
    
class Hand:
    def __init__(self, cards):
        self.cards = cards
        
    def add_card(self, card):
        self.cards.append(card)
        
    def remove_card(self, card):
        self.cards.remove(card)
        
    def __str__(self):
        return ', '.join([str(card) for card in self.cards])
    
    def sort_hand(self):
        self.cards.sort()
        
    def show_short_hand(self):
        return ', '.join([str(card) for card in sorted(self.cards)])
    
    

    
# Example usage
card1 = Card(10, 0x4)  # 10 of Hearts
card2 = Card(14, 0x8)  # Ace of Spades

print(f"Card 1: {card1}")  # Output: 10 of Hearts
print(f"Card 2: {card2}")  # Output: A of Spades

encoded_card1 = card1.encode()
print(f"Encoded Card 1: {encoded_card1:08b}")  # Binary representation

decoded_card1 = Card.decode(encoded_card1)
print(f"Decoded Card 1: {decoded_card1}")  # Output: 10 of Hearts

hand = [card1, card2, Card(12, 0x1)]
hand1 = Hand(hand)
print(f"hand: {hand1}")

hand1.sort_hand()
print(f"hand: {hand1}")