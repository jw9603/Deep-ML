'''
1. Matrix-Vector Dot Product

Write a Python function that computes the dot product of a matrix and a vector.
The function should return a list resulting vector if the operation is valid, or -1 if the matrix and vector dimensions are incompatible.
A matrix (a lost of lists) can be dotted with a vector (a list) only if the number of columns in the matrix equals the length of the vector.
For example, an n x m matrix requires a vector of length m. 
You may assume the input matrix is a valid (non-jagged) list of lists and the vector is a non-empty list.
'''

########################################### 1. NumPy Implementation ###########################################
def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
    # Return a list where each element is the dot product of a row of 'a' with 'b'.
    # If the number of columns in 'a' does not match the length of 'b', return -1.

    a_rows = len(a)
    a_cols = len(a[0]) if a_rows > 0 else 0
    b_length = len(b)
    
    if a_cols != b_length:
        return -1
    
    result = []
    for row in a:
        dot_product = sum(row[i] * b[i] for i in range(a_cols))
        result.append(dot_product)
    
    return result

########################################### 2. PyTorch Implementation ###########################################
import torch

def matrix_dot_vector(a, b) -> torch.Tensor:
    """
    Compute the product of matrix `a` and vector `b` using PyTorch.
    Inputs can be Python lists, NumPy arrays, or torch Tensors.
    Returns a 1-D tensor of length m, or tensor(-1) if dimensions mismatch.
    """
    a_t = torch.as_tensor(a, dtype=torch.float)
    b_t = torch.as_tensor(b, dtype=torch.float)
    # Dimension mismatch check
    if a_t.size(1) != b_t.size(0):
        return torch.tensor(-1)
    # Your implementation here
    result = torch.matmul(a_t, b_t)
    return result

if __name__ == "__main__":
    # Example usage:
    matrix = [[1, 2], [2, 4]]
    vector = [1, 2]
    
    result = matrix_dot_vector(matrix, vector)
    print(result)  # Output: [5, 10]
    
    # Incompatible dimensions example
    incompatible_vector = [1, 2, 3]
    result_incompatible = matrix_dot_vector(matrix, incompatible_vector)
    print(result_incompatible)  # Output: -1
    
    