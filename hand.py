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
    
    def __ls__(self, ):
        return self.rank < other.rank
    
    
# Example usage
card1 = Card(10, 0x4)  # 10 of Hearts
card2 = Card(14, 0x8)  # Ace of Spades

print(f"Card 1: {card1}")  # Output: 10 of Hearts
print(f"Card 2: {card2}")  # Output: A of Spades

encoded_card1 = card1.encode()
print(f"Encoded Card 1: {encoded_card1:08b}")  # Binary representation

decoded_card1 = Card.decode(encoded_card1)
print(f"Decoded Card 1: {decoded_card1}")  # Output: 10 of Hearts