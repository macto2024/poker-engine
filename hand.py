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
        return f"{Card.Ranks[self.Ranks]} of f{Card.Suits[self.Ranks]}"
    
    def encode(self):
        return self.suit << 4 | self.rank
    
    @classmethod
    def decode(self):
        ...
        
    