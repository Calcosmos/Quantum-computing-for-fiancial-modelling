import numpy as np

zero = np.array([1, 0])  # |0>
one = np.array([0, 1])   # |1>

def tensor_product(a, b):
    return np.kron(a, b)

# Bell state |ψ⟩ = (|00⟩ + |11⟩) / sqrt(2)
bell_state = (1 / np.sqrt(2)) * (tensor_product(zero, zero) + tensor_product(one, one))

# result
print("Bell State (|ψ⟩):")
print(bell_state)
