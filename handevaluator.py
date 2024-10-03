import numpy as np
from hand import Card

class HandEvaluator:
    
    # HIGHCARD      = 1
    # ONEPAIR       = 2
    # TWOPAIR       = 3
    # THREECARD     = 4
    # STRAIGHT      = 5
    # FLUSH         = 6
    # FULLHOUSE     = 7
    # FOURCARD      = 8
    # STRAIGHTFLASH = 9

    # HAND_STRENGTH_MAP = {
    #     HIGHCARD: "HIGHCARD",
    #     ONEPAIR: "ONEPAIR",
    #     TWOPAIR: "TWOPAIR",
    #     THREECARD: "THREECARD",
    #     STRAIGHT: "STRAIGHT",
    #     FLUSH: "FLUSH",
    #     FULLHOUSE: "FULLHOUSE",
    #     FOURCARD: "FOURCARD",
    #     STRAIGHTFLASH: "STRAIGHTFLASH"
    # }
    
    @classmethod
    def evaluate_best_hand(cls, cards):
        """Evaluate the best 5-card hand from a 7-card set and return the list of Card objects and hand rank string."""
        ranks = np.array([card.rank for card in cards])
        suits = np.array([card.suit for card in cards])
        
        rank_count = np.unique(ranks, return_counts=True)
        suit_count = np.unique(suits, return_counts=True)

        # Step 1: Check for Straight Flush
        flush_cards = cls.get_flush_cards(cards, suits)
        straight = cls.get_straight(cards)
        if flush_cards is not None and straight is not None:
            best_straight = flush_cards[:5]
            
            # Check for Royal Flush
            if set([14, 13, 12, 11, 10]).issubset([card.rank for card in best_straight]):
                return best_straight, "ROYALFLUSH"
            
            return best_straight, "STRAIGHTFLUSH"

        # Step 2: Check for Four of a Kind
        four_kind = cls.get_four_of_a_kind(rank_count, cards)
        if four_kind:
            return four_kind, "FOURCARD"

        # Step 3: Check for Full House
        full_house = cls.get_full_house(rank_count, cards)
        if full_house:
            return full_house, "FULLHOUSE"

        # Step 4: Check for Flush
        if flush_cards:
            return flush_cards[:5], "FLUSH"

        # Step 5: Check for Straight
        if straight is not None:
            return straight, "STRAIGHT"

        # Step 6: Check for Three of a Kind
        three_kind = cls.get_three_of_a_kind(rank_count, cards)
        if three_kind:
            return three_kind, "THREECARD"

        # Step 7: Check for Two Pair
        two_pair = cls.get_two_pair(rank_count, cards)
        if two_pair:
            return two_pair, "TWOPAIR"

        # Step 8: Check for One Pair
        one_pair = cls.get_one_pair(rank_count, cards)
        if one_pair:
            return one_pair, "ONEPAIR"

        # Step 9: High Card
        return cls.get_high_card(cards), "HIGHCARD"

    @classmethod
    def get_flush_cards(cls, cards, suits):
        """Return flush cards as Card objects if a flush is found."""
        suit, counts = np.unique(suits, return_counts=True)
        flush_suit = suit[counts >= 5]
        if len(flush_suit) == 0:
            return None
        flush_cards = [card for card in cards if card.suit == flush_suit[0]]
        return sorted(flush_cards, key=lambda x: x.rank, reverse=True)


    @classmethod
    def get_straight(cls, cards):
        """Return the best straight as Card objects."""
        ranks = np.array([card.rank for card in cards])
        unique_ranks = np.unique(ranks)
        sorted_ranks = np.sort(unique_ranks)

        # Check for a regular straight
        for i in range(len(sorted_ranks) - 4):
            if sorted_ranks[i + 4] - sorted_ranks[i] == 4:
                return sorted([card for card in cards if card.rank in sorted_ranks[i:i + 5]], key=lambda x: x.rank, reverse=True)

        # Check for Ace-low straight (A-2-3-4-5)
        if set([14, 2, 3, 4, 5]).issubset(sorted_ranks):
            return sorted([card for card in cards if card.rank in [14, 5, 4, 3, 2]], key=lambda x: x.rank, reverse=True)

        return None


    @classmethod
    def get_four_of_a_kind(cls, rank_count, cards):
        """Return the best four-of-a-kind as Card objects."""
        rank, counts = rank_count
        if 4 in counts:
            four_kind_rank = rank[counts == 4][0]
            four_kind = [card for card in cards if card.rank == four_kind_rank]
            kicker = cls.get_high_card([card for card in cards if card.rank != four_kind_rank])
            return four_kind + kicker[:1]
        return None

    @classmethod
    def get_full_house(cls, rank_count, cards):
        """Return the best full house as Card objects."""
        rank, counts = rank_count
        if 3 in counts and 2 in counts:
            three_of_a_kind_rank = rank[counts == 3][0]
            pair_rank = rank[counts == 2][0]
            three_of_a_kind = [card for card in cards if card.rank == three_of_a_kind_rank]
            pair = [card for card in cards if card.rank == pair_rank]
            return three_of_a_kind + pair[:2]
        return None

    @classmethod
    def get_three_of_a_kind(cls, rank_count, cards):
        """Return the best three-of-a-kind as Card objects."""
        rank, counts = rank_count
        if 3 in counts:
            three_kind_rank = rank[counts == 3][0]
            three_kind = [card for card in cards if card.rank == three_kind_rank]
            kickers = cls.get_high_card([card for card in cards if card.rank != three_kind_rank])
            return three_kind + kickers[:2]
        return None

    @classmethod
    def get_two_pair(cls, rank_count, cards):
        """Return the best two pairs as Card objects."""
        rank, counts = rank_count
        pairs = rank[counts == 2]
        if len(pairs) >= 2:
            top_two_pairs = sorted(pairs, reverse=True)[:2]
            two_pair = [card for card in cards if card.rank in top_two_pairs]
            kicker = cls.get_high_card([card for card in cards if card.rank not in top_two_pairs])
            return two_pair + kicker[:1]
        return None

    @classmethod
    def get_one_pair(cls, rank_count, cards):
        """Return the best one pair as Card objects."""
        rank, counts = rank_count
        if 2 in counts:
            pair_rank = rank[counts == 2][0]
            pair = [card for card in cards if card.rank == pair_rank]
            kickers = cls.get_high_card([card for card in cards if card.rank != pair_rank])
            return pair + kickers[:3]
        return None


    @classmethod
    def get_high_card(cls, cards):
        """Return the best high card hand as Card objects."""
        return sorted(cards, key=lambda x: x.rank, reverse=True)[:5]

##########################################################################

class HandRankEncoder:
    RANK_CODES = {
        "HIGHCARD": 1,
        "ONEPAIR": 2,
        "TWOPAIR": 3,
        "THREECARD": 4,
        "STRAIGHT": 5,
        "FLUSH": 6,
        "FULLHOUSE": 7,
        "FOURCARD": 8,
        "STRAIGHTFLUSH": 9,
        "ROYALFLUCH" : 10
    }

    CARD_RANKS = {
        1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
        10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E'
    }

    @classmethod
    def encode_hand(cls, hand_type, ranks):
        """
        Encodes the hand based on hand rank and sorted card ranks.

        Parameters:
        hand_type (str): The type of hand (e.g., "TWOPAIR", "FULLHOUSE")
        ranks (list): List of card that make up the hand 
        
        (e.g., [Card(14, 0x1),  # Ace of Spades
                Card(10, 0x2),  # 10 of Diamonds
                Card(8, 0x4),   # 8 of Hearts
                Card(5, 0x8),   # 5 of Clubs
                Card(7, 0x2),   # 7 of Diamonds])

        Returns:
        str: A 6-digit hexadecimal representation of the hand rank and sorted card ranks.
        """
        # Step 1: Get the hand rank code
        rank_code = cls.RANK_CODES.get(hand_type, 0)

        # Step 2: Convert the ranks to their respective hexadecimal values
        hex_ranks = ''.join(cls.CARD_RANKS[rank] for rank in ranks)

        # Step 3: Check for Ace-low straight (A-2-3-4-5)
        if hand_type == "STRAIGHT" and set(ranks) == {14, 5, 4, 3, 2}:
            # Modify to treat Ace as 1
            hex_ranks = ''.join(cls.CARD_RANKS[rank] for rank in [5, 4, 3, 2, 1])

        # Step 4: Combine the hand rank with the card ranks into a 6-digit hex code
        encoded_hand = f"{rank_code:X}{hex_ranks}"

        return encoded_hand

class HandRankDecoder:
    ...