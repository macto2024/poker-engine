import unittest
import pickle
from hand import Card
from handevaluator import HandRankDecoder
from look_up_table import LookUpTable

class TestLookUpTable(unittest.TestCase):
    
    def setUp(self):
        # Create an instance of LookUpTable
        self.lookup_table = LookUpTable()
        with open("lookup_table_test.pkl", "rb") as f:
            self.lookup_table.hand_lookup_table = pickle.load(f)

    def test_hand_in_lookup_table(self):
        # Define 20 test hands
        test_hands = [
            # High card hand
            [Card(14, 0x1), Card(10, 0x2), Card(8, 0x4), Card(5, 0x8), Card(7, 0x2)],  # Ace high
            # One pair hands
            [Card(14, 0x1), Card(14, 0x2), Card(10, 0x4), Card(8, 0x8), Card(5, 0x4)],  # Pair of Aces
            [Card(12, 0x1), Card(12, 0x4), Card(10, 0x2), Card(8, 0x8), Card(6, 0x1)],  # Pair of Queens
            # Two pair hands
            [Card(14, 0x1), Card(14, 0x2), Card(10, 0x4), Card(10, 0x8), Card(7, 0x1)], # Two pair Aces & Tens
            [Card(12, 0x2), Card(12, 0x4), Card(8, 0x1), Card(8, 0x2), Card(5, 0x8)],   # Two pair Queens & Eights
            # Three of a kind
            [Card(14, 0x1), Card(14, 0x2), Card(14, 0x4), Card(8, 0x8), Card(7, 0x1)],  # Three Aces
            [Card(10, 0x1), Card(10, 0x2), Card(10, 0x4), Card(7, 0x2), Card(5, 0x1)],  # Three Tens
            # Straight hands
            [Card(14, 0x1), Card(13, 0x2), Card(12, 0x4), Card(11, 0x8), Card(10, 0x1)],# Broadway straight (A-K-Q-J-10)
            [Card(5, 0x1), Card(4, 0x2), Card(3, 0x4), Card(2, 0x8), Card(14, 0x1)],    # Ace-low straight (A-2-3-4-5)
            # Flush hands
            [Card(14, 0x1), Card(10, 0x1), Card(8, 0x1), Card(6, 0x1), Card(3, 0x1)],   # Ace-high flush
            # Full house hands
            [Card(14, 0x1), Card(14, 0x2), Card(8, 0x4), Card(8, 0x2), Card(8, 0x1)],   # Full house Aces full of Eights
            [Card(12, 0x1), Card(12, 0x2), Card(6, 0x4), Card(6, 0x2), Card(6, 0x1)],   # Full house Queens full of Sixes
            # Four of a kind
            [Card(14, 0x1), Card(14, 0x2), Card(14, 0x4), Card(14, 0x8), Card(10, 0x1)],# Four of a kind Aces
            [Card(9, 0x1), Card(9, 0x2), Card(9, 0x4), Card(9, 0x8), Card(5, 0x1)],     # Four of a kind Nines
            # Straight flush hands
            [Card(9, 0x1), Card(8, 0x1), Card(7, 0x1), Card(6, 0x1), Card(5, 0x1)],     # 9-high straight flush
            [Card(5, 0x2), Card(4, 0x2), Card(3, 0x2), Card(2, 0x2), Card(14, 0x2)],    # Ace-low straight flush (A-2-3-4-5)
            # Royal flush hands
            [Card(14, 0x1), Card(13, 0x1), Card(12, 0x1), Card(11, 0x1), Card(10, 0x1)],# Royal flush Spades
            [Card(14, 0x4), Card(13, 0x4), Card(12, 0x4), Card(11, 0x4), Card(10, 0x4)],# Royal flush Hearts
        ]
        
        # Test each hand in the lookup table
        for hand in test_hands:
            encoded_hand_key = self.lookup_table.encode_hand(hand)
            #convert hand to human readable cards
            hand_representation = ', '.join([str(card) for card in hand]) 
            if encoded_hand_key not in self.lookup_table.hand_lookup_table:
                print(f"Hand {hand_representation} not found in lookup table.")
            else:
                encoded_rank = self.lookup_table.hand_lookup_table[encoded_hand_key]
                hand_type, ranks = HandRankDecoder.decode_hand(encoded_rank)
                print(f"Hand: ({hand_representation}) Rank: {hand_type} Encoded Rank: {self.lookup_table.hand_lookup_table[encoded_hand_key]}")
            self.assertIn(encoded_hand_key, self.lookup_table.hand_lookup_table)


if __name__ == '__main__':
    unittest.main()


#########################################################

# lookup = LookUpTable()

# with open("lookup_table_test.pkl", "rb") as f:
#     lookup_table = pickle.load(f)
    
# lookup.hand_lookup_table = lookup_table

# # Pick a specific hand to test
# test_hand = [
#     Card(3, 0x2),  # 2 of Spades
#     Card(3, 0x1),  # 3 of Diamonds
#     Card(4, 0x4),  # 4 of Hearts
#     Card(4, 0x8),  # 5 of Clovers
#     Card(6, 0x2)   # 6 of Spades
# ]


# # Encode the test hand
# encoded_key = lookup.encode_hand(test_hand)

# # Lookup the hand in the table
# if encoded_key in lookup.hand_lookup_table:
#     print(f"Found hand in lookup table. Encoded Rank: {lookup.hand_lookup_table[encoded_key]}")
# else:
#     print("Hand not found in lookup table.")

#######################################################################

# print("chekcing lookup_table_test.pkl")

# # Load and inspect the contents of the pickle file
# with open("lookup_table_test.pkl", "rb") as f:
#     lookup_table = pickle.load(f)

# # Check how many entries there are
# print(f"Total entries in lookup table: {len(lookup_table)}")

# # Display the first few entries to get an idea of the data structure
# for key, value in list(lookup_table.items())[:10]:  # Adjust the slice to show more/less entries
#     print(f"Key: {key}, Value: {value}")