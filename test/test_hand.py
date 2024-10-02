from hand import Card, Hand

################ Example usage for hand.py###############

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
print(f"hand before sort: {hand1}")

hand1.sort_hand()
print(f"hand after sort: {hand1}")

###########################################################
