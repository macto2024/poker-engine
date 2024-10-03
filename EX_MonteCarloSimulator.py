from hand import Card
from MonteCarloSimulator import MonteCarloSimulator

# Define the hole cards for two players
player_hands = [
    [Card(14, 1), Card(13, 2)],  # Player 1: Ace of Spades and King of Diamonds
    [Card(10, 4), Card(9, 8)]    # Player 2: 10 of Hearts and 9 of Clubs
]

# Create the simulator
simulator = MonteCarloSimulator(player_hands)

# Run the simulation
num_simulations = 100000  # You can change this to a higher number for more accurate results
results, tie_info = simulator.simulate(num_simulations)

# Output the results
for player, win_rate in results.items():
    print(f"{player}: {win_rate * 100:.2f}% win rate")

print(f"Tie Rate: {tie_info['Tie Rate'] * 100:.2f}%")

