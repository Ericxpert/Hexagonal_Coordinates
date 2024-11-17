import numpy as np
from scipy.optimize import linear_sum_assignment

def best_matching(scores):
    # Convert scores to a numpy array
    scores = np.array(scores)
    # Use the Hungarian algorithm to find the best matching
    row_ind, col_ind = linear_sum_assignment(-scores)
    # Return the matched pairs and the total score
    total_score = scores[row_ind, col_ind].sum()
    matches = list(zip(row_ind, col_ind))
    return matches, total_score

# Example usage
# Define the scores matrix where rows are matchers and columns are matchees
scores = [
    [9, 11, 14, 11, 7],
    [6, 15, 13, 13, 10],
    [12, 13, 6, 8, 8],
    [11, 9, 10, 12, 9],
    [7, 12, 14, 10, 14]
]

matches, total_score = best_matching(scores)
print("Matches:", matches)
print("Total Score:", total_score)
