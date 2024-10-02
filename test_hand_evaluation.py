
from handevaluator import HandRankEncoder, HandEvaluator
from hand import Card

################# Example usage for hand encoder #########################

# # Two Pair: K, K, 10, 10, 5
# encoded_hand_1 = HandRankEncoder.encode_hand("TWOPAIR", [13, 13, 10, 10, 5])
# print(f"Encoded Hand (Two Pair): {encoded_hand_1}")  # Output: 3DDAA5

# # Full House: 2, 5, 2, 5, 2
# encoded_hand_2 = HandRankEncoder.encode_hand("FULLHOUSE", [2, 5, 2, 5, 2])
# print(f"Encoded Hand (Full House): {encoded_hand_2}")  # Output: 722255


############ Example card objects (create your Card objects here) ###############
cards_starigt = [
    Card(14, 0x1),  # Ace of Spades (A♠)
    Card(13, 0x4),  # King of Hearts (K♥)
    Card(12, 0x2),  # Queen of Diamonds (Q♦)
    Card(11, 0x1),  # Jack of Spades (J♠)
    Card(10, 0x8),  # 10 of Clovers (10♣)
    Card(3, 0x4),   # 3 of Hearts (3♥)
    Card(7, 0x1)    # 7 of Spades (7♠)
]

cards_ace_low_straight = [
    Card(14, 0x1),  # Ace of Spades
    Card(2, 0x2),   # 2 of Diamonds
    Card(3, 0x4),   # 3 of Hearts
    Card(4, 0x8),   # 4 of Clubs
    Card(5, 0x1),   # 5 of Spades
    Card(9, 0x2),   # 9 of Diamonds (irrelevant for straight)
    Card(7, 0x1)    # 7 of Spades (irrelevant for straight)
]

cards_high_card = [
    Card(14, 0x1),  # Ace of Spades
    Card(10, 0x2),  # 10 of Diamonds
    Card(8, 0x4),   # 8 of Hearts
    Card(5, 0x8),   # 5 of Clubs
    Card(7, 0x2),   # 7 of Diamonds
    Card(2, 0x1),   # 2 of Spades
    Card(9, 0x4)    # 9 of Hearts
]

cards_one_pair = [
    Card(14, 0x1),  # Ace of Spades
    Card(14, 0x2),  # Ace of Diamonds
    Card(10, 0x4),  # 10 of Hearts
    Card(8, 0x8),   # 8 of Clubs
    Card(5, 0x4),   # 5 of Hearts
    Card(3, 0x1),   # 3 of Spades
    Card(6, 0x2)    # 6 of Diamonds
]

cards_two_pair = [
    Card(14, 0x1),  # Ace of Spades
    Card(14, 0x2),  # Ace of Diamonds
    Card(10, 0x4),  # 10 of Hearts
    Card(10, 0x8),  # 10 of Clubs
    Card(7, 0x1),   # 7 of Spades
    Card(5, 0x2),   # 5 of Diamonds
    Card(3, 0x4)    # 3 of Hearts
]

cards_three_of_a_kind = [
    Card(12, 0x1),  # Queen of Spades
    Card(12, 0x2),  # Queen of Diamonds
    Card(12, 0x4),  # Queen of Hearts
    Card(8, 0x8),   # 8 of Clubs
    Card(5, 0x2),   # 5 of Diamonds
    Card(3, 0x1),   # 3 of Spades
    Card(7, 0x4)    # 7 of Hearts
]

cards_flush = [
    Card(14, 0x1),  # Ace of Spades
    Card(10, 0x1),  # 10 of Spades
    Card(8, 0x1),   # 8 of Spades
    Card(6, 0x1),   # 6 of Spades
    Card(3, 0x1),   # 3 of Spades
    Card(2, 0x4),   # 2 of Hearts
    Card(5, 0x2)    # 5 of Diamonds
]

cards_full_house = [
    Card(13, 0x1),  # King of Spades
    Card(13, 0x4),  # King of Hearts
    Card(8, 0x8),  # King of Clubs
    Card(8, 0x2),   # 8 of Diamonds
    Card(8, 0x4),   # 8 of Hearts
    Card(3, 0x1),   # 3 of Spades
    Card(5, 0x8)    # 5 of Clubs
]

cards_four_of_a_kind = [
    Card(9, 0x1),   # 9 of Spades
    Card(9, 0x2),   # 9 of Diamonds
    Card(9, 0x4),   # 9 of Hearts
    Card(9, 0x8),   # 9 of Clubs
    Card(12, 0x1),  # Queen of Spades
    Card(3, 0x2),   # 3 of Diamonds
    Card(5, 0x4)    # 5 of Hearts
]

cards_straight_flush = [
    Card(9, 0x1),   # 9 of Spades
    Card(8, 0x1),   # 8 of Spades
    Card(7, 0x1),   # 7 of Spades
    Card(6, 0x1),   # 6 of Spades
    Card(5, 0x1),   # 5 of Spades
    Card(3, 0x2),   # 3 of Diamonds
    Card(4, 0x4)    # 4 of Hearts
]

cards_royal_flush = [
    Card(14, 0x1),  # Ace of Spades
    Card(13, 0x1),  # King of Spades
    Card(12, 0x1),  # Queen of Spades
    Card(11, 0x1),  # Jack of Spades
    Card(10, 0x1),  # 10 of Spades
    Card(8, 0x4),   # 8 of Hearts
    Card(7, 0x8)    # 7 of Clubs
]



# Step 1: Evaluate the best hand using HandEvaluator
best_hand, hand_type = HandEvaluator.evaluate_best_hand(cards_ace_low_straight)

# Step 2: Print best hand as string
print(f"Best Hand: {', '.join([str(card) for card in best_hand])}")
print(f"Hand Type: {hand_type}")

# Extract the ranks from the best hand for encoding
best_hand_ranks = [card.rank for card in best_hand]
print(f"Best Hand Ranks: {best_hand_ranks}")

# Step 3: Encode the hand using HandRankEncoder
encoded_hand_rank = HandRankEncoder.encode_hand(hand_type, best_hand_ranks)
print(f"Encoded Hand Rank: {encoded_hand_rank}")
