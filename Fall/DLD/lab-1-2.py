import matplotlib.pyplot as plt
import pandas as pd


def save_truth_tables_as_images():
    # Define input combinations for 2 inputs (A and B)
    inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]

    # Prepare data for OR truth table
    or_data = {'A': [], 'B': [], 'A OR B': []}
    for A, B in inputs:
        or_data['A'].append(A)
        or_data['B'].append(B)
        or_data['A OR B'].append(A | B)

    # Create a DataFrame for OR truth table
    or_table = pd.DataFrame(or_data)

    # Plot OR truth table
    plt.figure(figsize=(5, 3))
    plt.axis('tight')
    plt.axis('off')
    the_table = plt.table(cellText=or_table.values, colLabels=or_table.columns, cellLoc='center', loc='center')
    the_table.auto_set_font_size(False)
    the_table.set_fontsize(12)
    plt.title("OR Truth Table", fontsize=14)
    plt.savefig("or_truth_table.png", bbox_inches='tight')
    plt.close()

    # Prepare data for NOR truth table
    nor_data = {'A': [], 'B': [], 'A NOR B': []}
    for A, B in inputs:
        nor_data['A'].append(A)
        nor_data['B'].append(B)
        nor_data['A NOR B'].append(int(not (A | B)))

    # Create a DataFrame for NOR truth table
    nor_table = pd.DataFrame(nor_data)

    # Plot NOR truth table
    plt.figure(figsize=(5, 3))
    plt.axis('tight')
    plt.axis('off')
    the_table = plt.table(cellText=nor_table.values, colLabels=nor_table.columns, cellLoc='center', loc='center')
    the_table.auto_set_font_size(False)
    the_table.set_fontsize(12)
    plt.title("NOR Truth Table", fontsize=14)
    plt.savefig("nor_truth_table.png", bbox_inches='tight')
    plt.close()


# Call the function to create and save the truth tables as images
save_truth_tables_as_images()
