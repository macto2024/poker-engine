import random
import itertools
import pickle

from look_up_table import LookUpTable
from hand import Card

class MonteCarloSimulator:
    def __init__(self, player_hands):
        """
        Initialize the simulator with multiple player's hole cards and look up table.
        player_hands: List of lists, each containing two Card objects representing the player's hole cards.
        """
        if not all(len(hand) == 2 for hand in player_hands):
            raise ValueError("Each player must have exactly two hole cards.")
        
        self.player_hands = player_hands
        # deck excluding player's hands
        self.rest_deck = self.__generate_full_deck([card for hand in player_hands for card in hand])
        #look up table
        self.lookup_table = LookUpTable()
        with open("lookup_table_test.pkl", "rb") as f:
            self.lookup_table.hand_lookup_table = pickle.load(f)
        

    def __generate_full_deck(self, exclude_cards):
        """Generate a full deck of 52 cards, excluding the cards that are already in use."""
        suits = [1, 2, 4, 8]  # Suits: Spades, Diamonds, Hearts, Clubs
        ranks = range(2, 15)   # 2 to Ace
        deck = [Card(rank, suit) for rank in ranks for suit in suits]
        return [card for card in deck if card not in exclude_cards]    

    def simulate(self, num_simulations=1000):
        """
        Run the Monte Carlo simulation to calculate the winning probabilities for each player.
        num_simulations: Number of random simulations to run.
        """
        num_players = len(self.player_hands)
        player_wins = [0] * num_players  # Track wins for each player
        ties = 0

        deck = self.rest_deck

        for _ in range(num_simulations):
            # Draw 5 random community cards
            community_cards = random.sample(deck, 5)

            # Evaluate the hands for all players
            hand_strengths = self.__evaluate_hands(community_cards)

            # Determine the best hand and check for ties
            max_strength = max(hand_strengths)
            winners = [i for i, strength in enumerate(hand_strengths) if strength == max_strength]

            if len(winners) == 1:
                player_wins[winners[0]] += 1
            else:
                ties += 1

        total_simulations = num_simulations
        return {
            f"Player {i+1} Win Rate": player_wins[i] / total_simulations for i in range(num_players)
        }, {"Tie Rate": ties / total_simulations}

    def __generate_full_deck(self, exclude_cards):
        """Generate a full deck of 52 cards, excluding the cards that are already in use."""
        suits = [1, 2, 4, 8]  # Suits: Spades, Diamonds, Hearts, Clubs
        ranks = range(2, 15)   # 2 to Ace
        deck = [Card(rank, suit) for rank in ranks for suit in suits]
        return [card for card in deck if card not in exclude_cards]
    
    def __evaluate_hands(self, community_cards):
        """
        Evaluate each player's best hand by combining their hole cards with the community cards.
        Instead of evaluating dynamically, it looks up the best 5-card combination using a precomputed lookup table.
        return each players best encoded hand
        """
        hand_strengths = []
        
        for hand in self.player_hands:
            # Combine hole cards and community cards
            total_cards = hand + community_cards
            
            # Generate all 5-card combinations from the 7 cards
            all_combinations = itertools.combinations(total_cards, 5)
            
            best_hand_strength = None
            best_encoded_hand = None
            
            # Iterate over all combinations, lookup each in the lookup table, and track the best
            for combination in all_combinations:
                encoded_hand_key = self.lookup_table.encode_hand(combination)
                
                # Lookup the hand in the precomputed lookup table
                if encoded_hand_key in self.lookup_table.hand_lookup_table:
                    encoded_hand_rank = self.lookup_table.hand_lookup_table[encoded_hand_key]
                    
                    # Compare ranks and keep track of the best hand
                    if best_hand_strength is None or encoded_hand_rank > best_hand_strength:
                        best_hand_strength = encoded_hand_rank
                        best_encoded_hand = encoded_hand_key

            # Append the best hand's strength
            hand_strengths.append(best_hand_strength)

        return hand_strengths

