import itertools
import multiprocessing as mp
import pickle  # For persistent storage
from hand import Card
from handevaluator import HandEvaluator, HandRankEncoder

class LookUpTable:
    def __init__(self):
        self.hand_lookup_table = {}

    def add_hand_to_lookup_table(self, hand):
        """
        Add a hand to the lookup table by encoding the hand as a key and storing the
        evaluated hand rank as the value.
        """
        encoded_hand_key = self.encode_hand(hand)
        best_hand, hand_type = HandEvaluator.evaluate_best_hand(hand)
        best_hand_ranks = [card.rank for card in best_hand]
        encoded_hand_rank = HandRankEncoder.encode_hand(hand_type, best_hand_ranks)
        self.hand_lookup_table[encoded_hand_key] = encoded_hand_rank

    # def add_hand_to_lookup_table(self, hand):
    #     """ Add a hand to the lookup table. """
    #     # Step 1: Encode the hand
    #     encoded_hand_key = self.encode_hand(hand)

    #     # Step 2: Evaluate the hand using HandEvaluator
    #     best_hand, hand_type = HandEvaluator.evaluate_best_hand(hand)
    #     print(f"Processing hand: {hand}, Best Hand: {best_hand}, Hand Type: {hand_type}")

    #     # Step 3: Extract ranks from best hand
    #     best_hand_ranks = [card.rank for card in best_hand]

    #     # Step 4: Encode the hand using HandRankEncoder
    #     encoded_hand_rank = HandRankEncoder.encode_hand(hand_type, best_hand_ranks)
    #     print(f"Encoded Hand Rank: {encoded_hand_rank}")

    #     # Step 5: Store in lookup table
    #     self.hand_lookup_table[encoded_hand_key] = encoded_hand_rank
    #     print(f"Added {encoded_hand_key} -> {encoded_hand_rank} to lookup table")

    def encode_hand(self, hand):
        """
        Encode a 5-card hand into a 40-bit integer representation.
        
        Each card is encoded as an 8-bit integer using the Card's encode method.
        The hand is then combined into a 40-bit integer by shifting and adding the encoded cards.
        """
        if len(hand) != 5:
            raise ValueError("A hand must consist of exactly 5 cards.")

        encoded_hand = 0
        sorted_hand = sorted(hand, key=lambda card: (card.rank, card.suit), reverse=True)
        for card in sorted_hand:
            encoded_card = card.encode()
            encoded_hand = (encoded_hand << 8) | encoded_card
        return encoded_hand

    def process_hand(self, hand):
        """Multiprocessing helper function to process and add a hand to the lookup table."""
        return self.add_hand_to_lookup_table(hand)

    def create_lookup_table(self):
        """
        Generate the first 'num_combinations' 5-card combinations from the deck and populate the lookup table.
        """
        suits = [1, 2, 4, 8]  # Spades, Diamonds, Hearts, Clovers
        ranks = range(2, 15)  # 2 to Ace (14)
        deck = [Card(rank, suit) for rank in ranks for suit in suits]

        # Generate all possible 5-card combinations
        five_card_combinations = itertools.combinations(deck, 5)

        for count, combination in enumerate(five_card_combinations):
            self.add_hand_to_lookup_table(combination)

        return self.hand_lookup_table
    
    ############ multiprocess creation #########################################
    # def create_lookup_table(self):
    #     """Generate all 5-card combinations from the deck and populate the lookup table."""
    #     suits = [1, 2, 4, 8]  # Spades, Diamonds, Hearts, Clovers
    #     ranks = range(2, 15)  # 2 to Ace (14)
    #     deck = [Card(rank, suit) for rank in ranks for suit in suits]

    #     five_card_combinations = itertools.combinations(deck, 5)

    #     # Use multiprocessing to process the combinations in parallel
    #     with mp.Pool(mp.cpu_count()) as pool:
    #         results = pool.map(self.process_hand, five_card_combinations)

    #     # Store results in the lookup table
    #     self.hand_lookup_table = dict(results)

######################### This only creates first NUMCOM combination of 5 cards to test the table ################
    #NUMCOM = 1000
    def create_partial_lookup_table(self, num_combinations):
        """
        Generate the first 'num_combinations' 5-card combinations from the deck and populate the lookup table.
        """
        suits = [1, 2, 4, 8]  # Spades, Diamonds, Hearts, Clovers
        ranks = range(2, 15)  # 2 to Ace (14)
        deck = [Card(rank, suit) for rank in ranks for suit in suits]

        # Generate all possible 5-card combinations
        five_card_combinations = itertools.combinations(deck, 5)

        # Add only the first 'num_combinations' to the lookup table
        for count, combination in enumerate(five_card_combinations):
            if count >= num_combinations:
                break
            self.add_hand_to_lookup_table(combination)

        return self.hand_lookup_table
####################################################################################################################

    def save_lookup_table(self, filename='lookup_table.pkl'):
        """Save the lookup table to a file for persistent storage."""
        with open(filename, 'wb') as f:
            pickle.dump(self.hand_lookup_table, f)

    def load_lookup_table(self, filename='lookup_table.pkl'):
        """Load the lookup table from a file."""
        with open(filename, 'rb') as f:
            self.hand_lookup_table = pickle.load(f)