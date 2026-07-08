# Deep-ML Solutions

My solutions to [Deep-ML](https://www.deep-ml.com/problems) — machine learning coding challenges where each function is implemented from scratch.

The goal is not just to pass the grader, but to understand what each operation does mathematically and how production libraries implement it differently (numerical stability, views vs. copies, etc.).

## Convention

Each file corresponds to one problem and contains:

- The problem statement as a module docstring.
- A **NumPy / pure-Python** implementation.
- A **PyTorch** implementation, where applicable.

Filenames follow the problem title in `snake_case`.

## Progress

| # | Problem | Category | Difficulty | File |
|---|---------|----------|------------|------|
| 1 | [Matrix-Vector Dot Product](https://www.deep-ml.com/problems/1) | Linear Algebra | easy | [matrix-vector_dot_product.py](matrix-vector_dot_product.py) |
| 2 | [Transpose of a Matrix](https://www.deep-ml.com/problems/2) | Linear Algebra | easy | [transpose_of_a_matrix.py](transpose_of_a_matrix.py) |
| 3 | [Reshape Matrix](https://www.deep-ml.com/problems/3) | Linear Algebra | easy | [reshape_matrix.py](reshape_matrix.py) |
| 4 | [Calculate Mean by Row or Column](https://www.deep-ml.com/problems/4) | Linear Algebra | easy | [calculate_mean_by_row_or_column.py](calculate_mean_by_row_or_column.py) |

## Running

```bash
python3 matrix-vector_dot_product.py
```

PyTorch implementations require `torch`:

```bash
pip install torch
```

(On Deep-ml the grader runs in-browser via Pyodide, where `torch` is already available.)
