import matplotlib.pyplot as plt
from hand import Card
from MonteCarloSimulator import MonteCarloSimulator  # Assuming MonteCarloSimulator class is in monte_carlo_simulator.py

def get_card_input(player_num, card_num):
    """
    Helper function to get user input for a card (rank and suit).
    Returns a Card object.
    """
    while True:
        try:
            rank = input(f"Enter rank for Player {player_num}'s card {card_num} (e.g., 2-10, J, Q, K, A): ").strip().upper()
            suit = input(f"Enter suit for Player {player_num}'s card {card_num} (s=Spades, d=Diamonds, h=Hearts, c=Clubs): ").strip().lower()

            rank_value = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}[rank]
            suit_value = {'s': 1, 'd': 2, 'h': 4, 'c': 8}[suit]
            
            return Card(rank_value, suit_value)
        except (KeyError, ValueError):
            print("Invalid input. Please try again.")

def collect_player_hands(num_players):
    """
    Collect two cards for each player and ensure valid input.
    """
    player_hands = []
    for i in range(1, num_players + 1):
        hand = []
        while len(hand) < 2:  # Ensure exactly two cards per player
            try:
                card_1 = get_card_input(i, 1)
                card_2 = get_card_input(i, 2)
                hand = [card_1, card_2]
            except Exception as e:
                print(f"Error: {e}. Please enter the cards again.")
        player_hands.append(hand)
    return player_hands

# Main simulation loop
def run_simulation():
    num_players = int(input("Enter the number of players: "))

    if num_players < 2:
        print("The game requires at least 2 players.")
        return
    
    player_hands = collect_player_hands(num_players)

    # Create the Monte Carlo Simulator with the collected player hands
    simulator = MonteCarloSimulator(player_hands)
    
    # Simulate the game
    num_simulations = int(input("Enter the number of simulations: "))
    results, ties = simulator.simulate(num_simulations)

    # Display the results
    for player, win_rate in results.items():
        print(f"{player}: {win_rate * 100:.2f}% win rate")

    print(f"Tie Rate: {ties['Tie Rate'] * 100:.2f}%")

    # Visualize results with matplotlib
    labels = [f"Player {i + 1}" for i in range(num_players)]
    win_rates = [results[f"Player {i + 1} Win Rate"] * 100 for i in range(num_players)]
    plt.bar(labels, win_rates)
    plt.title('Win Rates of Players')
    plt.ylabel('Win Rate (%)')
    plt.show()

if __name__ == "__main__":
    run_simulation()
