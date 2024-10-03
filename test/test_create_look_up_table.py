import unittest
from look_up_table import LookUpTable
from hand import Card

class TestLookUpTable(unittest.TestCase):

    def setUp(self):
        """Set up a fresh lookup table for each test."""
        self.lookup_table = LookUpTable()

    def test_add_hand_to_lookup_table(self):
        """Test if a hand is added to the lookup table and returns the correct key and value."""
        # Sample 5-card hand
        hand = [
            Card(14, 0x1),  # Ace of Spades
            Card(10, 0x2),  # 10 of Diamonds
            Card(8, 0x4),   # 8 of Hearts
            Card(5, 0x8),   # 5 of Clovers
            Card(7, 0x2)    # 7 of Diamonds
        ]

        # Add hand to lookup table
        encoded_key, encoded_value = self.lookup_table.add_hand_to_lookup_table(hand)

        # Ensure that the hand was added correctly
        self.assertIn(encoded_key, self.lookup_table.hand_lookup_table)
        self.assertEqual(self.lookup_table.hand_lookup_table[encoded_key], encoded_value)

    def test_create_lookup_table(self):
        """Test if the lookup table is populated with all possible combinations of 5-card hands."""
        # Create the lookup table
        self.lookup_table.create_lookup_table()

        # There are 52 choose 5 possible hands, which is 2,598,960
        self.assertEqual(len(self.lookup_table.hand_lookup_table), 2598960)

if __name__ == '__main__':
    unittest.main()