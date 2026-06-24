'''
2. Transpose of a Matrix

Write a Python function that computes the transpose of a given 2D matrix. 
The transpose of a matrix is formed by turning its rows into columns and columns into rows. 
For an mxn matrix, the transpose will be a nxm matrix.
'''

############################################ 1. NumPy Implementation ###########################################
def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    if not a or not a[0]:
        return []
    return [[a[i][j] for i in range(len(a))] for j in range(len(a[0]))]

############################################ 2. PyTorch Implementation ###########################################
import torch

def transpose_matrix(a) -> torch.Tensor:
    """
    Transpose a 2D matrix using PyTorch.
    
    Args:
        a: A 2D matrix (can be list, numpy array, or torch.Tensor)
    
    Returns:
        A transposed torch.Tensor
    """
    a_t = torch.as_tensor(a)
    return a_t.t()


if __name__ == "__main__":
    # Example usage:
    matrix = [[1, 2, 3], [4, 5, 6]]
    transposed = transpose_matrix(matrix)
    print(transposed)  # Output: [[1, 4], [2, 5], [3, 6]]
