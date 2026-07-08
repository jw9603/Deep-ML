'''
4. Calculate Mean by Row or Column

Write a Python function that calculates the mean of a matrix either by row or by column, based on a given mode.
The function should take a matrix (list of lists) and a mode('row' or 'column') as input and return a list of means according to the specified mode.
'''

############################################ 1. NumPy Implementation ###########################################
import numpy as np
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:    
	return np.mean(matrix, axis=1) if mode == 'row' else np.mean(matrix, axis=0)


############################################ 2. PyTorch Implementation ###########################################
import torch

def calculate_matrix_mean(matrix, mode: str) -> torch.Tensor:
    """
    Calculate mean of a 2D matrix per row or per column using PyTorch.
    Inputs can be Python lists, NumPy arrays, or torch Tensors.
    Returns a 1-D tensor of means or raises ValueError on invalid mode.
    """
    a_t = torch.as_tensor(matrix, dtype=torch.float)
    # Your implementation here
    if mode == "row":
        return torch.mean(a_t, dim=1)
    elif mode == "column":
        return torch.mean(a_t, dim=0)
    else:
        raise ValueError("Mode must be 'row' or 'column'")

if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6]]
    mode = 'column'
    
    print(calculate_matrix_mean(matrix, mode))  # Output: [2.5, 3.5, 4.5]
    

