'''
3. Reshape Matrix

Write a Python function that reshapes a given matrix into a specified shape. if it can't be reshaped return back an empty list `[]`
'''

############################################ 1. NumPy Implementation ###########################################
import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	# Write your code here and return a python list after reshaping by using numpy's tolist() method
    try:
        return np.array(a).reshape(*new_shape)
    except ValueError:
        return []

############################################ 2. PyTorch Implementation ###########################################
import torch

def reshape_matrix(a, new_shape) -> torch.Tensor:
    """
    Reshape a 2D matrix `a` to shape `new_shape` using PyTorch.
    Inputs can be Python lists, NumPy arrays, or torch Tensors.
    Returns a tensor of shape `new_shape`, or an empty tensor on mismatch.
    """
    # Dimension check
    if len(a) * len(a[0]) != new_shape[0] * new_shape[1]:
        return torch.tensor([])
    # Convert to tensor and reshape
    a_t = torch.as_tensor(a, dtype=torch.float)
    # Your implementation here
    return a_t.reshape(*new_shape)
 
if __name__ == '__main__':
    a = [[1,2,3,4],[5,6,7,8]]
    new_shape = (4, 2)
    print(reshape_matrix(a, new_shape))