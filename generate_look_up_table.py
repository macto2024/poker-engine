from look_up_table import LookUpTable
from hand import Card

import pickle

lookup = LookUpTable()

# ################# Create instance of the lookup table ##################
# n = 200000
# # Create lookup table with first n combinations
# print(f"Generating lookup table for first {n} combinations...")
# lookup.create_partial_lookup_table(n)

# # Save the lookup table to a file
# lookup.save_lookup_table("lookup_table_test.pkl")
# print("Lookup table saved as lookup_table_test.pkl")


################ Create full lookup table total 52 C 5 #####################
print("Generating lookup table for first all combinations...")
lookup.create_lookup_table()

# Save the lookup table to a file
lookup.save_lookup_table("lookup_table.pkl")
print("Lookup table saved as lookup_table_test.pkl")