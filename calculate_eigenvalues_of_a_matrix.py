'''
6. Calculate Eigenvalues of a Matrix

Write a Python function that calculates the eigenvalues of a 2 x 2 matrix. The function should return a list
containing the eigenvalues, sort values from highest to lowest.
'''
import numpy as np
############################################ 1. NumPy Implementation ###########################################
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
    return sorted(np.linalg.eig(matrix)[0], reverse=True)

############################################ 2. PyTorch Implementation ###########################################
import torch

def calculate_eigenvalues(matrix: torch.Tensor) -> torch.Tensor:
    """
    Compute eigenvalues of a 2x2 matrix using PyTorch.
    Input: 2x2 tensor; Output: 1-D tensor with the two eigenvalues in descending order (highest to lowest).
    """
    # Your implementation here
    matrix = torch.as_tensor(matrix, dtype=torch.float64)
    eigenvalues = torch.linalg.eigvals(matrix).real
    return torch.sort(eigenvalues, descending=True).values


if __name__ == '__main__':
    # Example usage:
    matrix = [[2, 1], [1, 2]]
    print(calculate_eigenvalues(matrix))  # Output: [3.0, 1.0]