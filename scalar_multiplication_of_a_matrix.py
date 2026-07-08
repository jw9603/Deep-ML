'''
5. Scalar Multiplication of a Matrix

Write a Python function that multiplies a matrix by a scalar and returns the result.
'''
############################################ 1. NumPy Implementation ###########################################
import numpy as np
def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	# Your code here
	return np.array(matrix) * scalar


############################################ 2. PyTorch Implementation ###########################################
import torch

def scalar_multiply(matrix, scalar) -> torch.Tensor:
    """
    Multiply each element of a 2D matrix by a scalar using PyTorch.
    Inputs can be Python lists, NumPy arrays, or torch Tensors.
    Returns a 2D tensor of the same shape.
    """
    # Convert input to tensor
    m_t = torch.as_tensor(matrix, dtype=torch.float)
    # Your implementation here
    return m_t * scalar



if __name__ == '__main__':
    matrix, scalar = [[1, 2], [3, 4]], 2
    print(scalar_multiply(matrix, scalar)) # Output: [[2, 4], [6, 8]]