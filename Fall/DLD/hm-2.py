# Python code to generate the truth table for the given circuit
from itertools import product

# Define the truth table headers
headers = [
    "A", "B", "C", "D", "~B", "~D", "T1 = A & ~B", "T2 = C & ~D", "T3 = T1 | T2", "T4 = B ^ D", "F1 = T3 | T4", "F2 = ~A"
]

# Generate all possible combinations of inputs (A, B, C, D)
inputs = list(product([0, 1], repeat=4))

# Function to calculate each output based on the logic gates
def calculate_outputs(A, B, C, D):
    not_B = int(not B)
    not_D = int(not D)
    T1 = A & not_B
    T2 = C & not_D
    T3 = T1 | T2
    T4 = B ^ D
    F1 = T3 | T4
    F2 = int(not A)
    return [not_B, not_D, T1, T2, T3, T4, F1, F2]

# Create the truth table
truth_table = []
for inp in inputs:
    A, B, C, D = inp
    outputs = calculate_outputs(A, B, C, D)
    truth_table.append(list(inp) + outputs)

# Print the truth table
print(" | ".join(headers))
print("-" * 100)
for row in truth_table:
    print(" | ".join(map(str, row)))
