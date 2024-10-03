import itertools
from hand import Card
from handevaluator import HandEvaluator, HandRankEncoder

class LookUpTable:
    
    def __init__(self):
        # Initialize an empty lookup table
        self.hand_lookup_table = {}

    def add_hand_to_lookup_table(self, hand):
        """
        Add a hand to the lookup table by encoding the hand as a key and storing the
        evaluated hand rank as the value.
        """
        # Step 1: Encode the hand to create a unique 40-bit key
        encoded_hand_key = self.encode_hand(hand)
        
        # Step 2: Evaluate the hand using HandEvaluator
        best_hand, hand_type = HandEvaluator.evaluate_best_hand(hand)
        
        # Step 3: Extract ranks from the best hand
        best_hand_ranks = [card.rank for card in best_hand]
        
        # Step 4: Encode the hand rank using HandRankEncoder
        encoded_hand_rank = HandRankEncoder.encode_hand(hand_type, best_hand_ranks)
        
        # Step 5: Add to the lookup table
        self.hand_lookup_table[encoded_hand_key] = encoded_hand_rank

        return encoded_hand_key, encoded_hand_rank

    def encode_hand(self, hand):
        """
        Encode a 5-card hand into a 40-bit integer representation.
        
        Each card is encoded as an 8-bit integer using the Card's encode method.
        The hand is then combined into a 40-bit integer by shifting and adding the encoded cards.
        """
        if len(hand) != 5:
            raise ValueError("A hand must consist of exactly 5 cards.")

        encoded_hand = 0

        # Sort the hand first by rank, then by suit to ensure consistency
        sorted_hand = sorted(hand, key=lambda card: (card.rank, card.suit), reverse=True)

        for card in sorted_hand:
            # Use the card's built-in encode method
            encoded_card = card.encode()
            # Shift the existing encoded_hand by 8 bits and add the new encoded card
            encoded_hand = (encoded_hand << 8) | encoded_card

        return encoded_hand

    def decode_hand(self, encoded_hand):
        """
        Decode a 40-bit encoded hand back into a list of Card objects.
        """
        hand = []
        for _ in range(5):
            # Get the last 8 bits to decode the card
            encoded_card = encoded_hand & 0xFF
            # Shift the encoded hand to remove the last 8 bits
            encoded_hand >>= 8
            # Decode the card and append to the hand
            card = Card.decode(encoded_card)
            hand.append(card)

        # Return the hand sorted by rank and suit
        return sorted(hand, key=lambda card: (card.rank, card.suit), reverse=True)

    def create_lookup_table(self):
        """
        Generate all 5-card combinations from the deck and populate the lookup table.
        """
        # Create the full deck of 52 cards
        suits = [1, 2, 4, 8]  # Spades, Diamonds, Hearts, Clovers
        ranks = range(2, 15)  # 2 to Ace (14)

        deck = [Card(rank, suit) for rank in ranks for suit in suits]

        # Generate all possible 5-card combinations
        five_card_combinations = itertools.combinations(deck, 5)

        # Populate the lookup table with each combination
        for combination in five_card_combinations:
            # Add each combination to the lookup table
            self.add_hand_to_lookup_table(combination)

        return self.hand_lookup_table

lookup_table = LookUpTable()
look = lookup_table.create_lookup_table()
